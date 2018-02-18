import re
import requests
from bs4 import BeautifulSoup as BS
from bs4.element import NavigableString
import logging
import random

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def uniqueid():
    seed = random.getrandbits(1)
    while True:
        yield seed
        seed += 1

uid = uniqueid()

def get_lyrics(artist, get_album_genre=False):
    
    """
    Example:
        lyrics = get_lyrics('madonna')
    """
    
    base_url = 'http://lyrics.wikia.com'
    url_ext = '/wiki/'

    search_url = base_url + url_ext + 'Special:Search?query=' + artist.replace(' ', '+')
    search_resp = requests.get(search_url)
    soup = BS(search_resp.content)
    results = soup.find_all('a', {'class': 'result-link'})
    
    artist_url = results[0].attrs['href']
    
    logging.info('GET Artist URL: ' + artist_url)
    
    req = requests.get(artist_url)
    resp = BS(req.content, 'html')
    
    genre = ''
    genre_tag = resp.find_all('table', {'class': 'artist-info-box'})
    if genre_tag:
        for atag in resp.find_all('table', {'class': 'artist-info-box'})[0].find_all('a'):
            if 'Category:Genre' in atag.attrs['href']:
                genre += ('|' if genre else genre) + atag.text
    
    albums = {}
    nodes = resp.find_all('div', {'id': 'mw-content-text'})[0].find_all()
    for node in nodes:
        if node.name == 'h2':
            if node.find_all('span'):
                a_tag = node.find_all('a')
                album_url_span = node.findChild('span', {'class': 'mw-headline'})
                album_url_a = album_url_span if not album_url_span else album_url_span.findChild('a')
                album_url = album_url_a if not album_url_a else album_url_a.attrs.get('href')
                title = 'Misc (0000)' if not a_tag else a_tag[0].text
                year_search = re.search('([0-9]{4})', title)
                album_year = None if not year_search else year_search.group(0)
                albums[title] = {}
                albums[title]['year'] = album_year
                albums[title]['album_url'] = None if not album_url else (base_url + album_url)
        if node.name == 'ol':
            for song in node:
                track_a = song.find_all('a')
                if not track_a: continue
                track_node = track_a[0]
                track_name = track_node.text
                track_href = track_node.get('href')
                if 'tracks' not in albums[title]:
                    albums[title]['tracks'] = {}
                albums[title]['tracks'][track_name] = track_href

    lyrics_obj = []
    try:
        album_keys = albums.keys()
        for album in album_keys:
            album_url = albums[album]['album_url']
            album_genre = ''
            if get_album_genre and album_url:

                album_req = requests.get(album_url)
                album_soup = BS(album_req.content)
                genre_tag = album_soup.find_all('div', {'id': 'mw-content-text'})
                if genre_tag:
                    for atag in album_soup.findChild('div', {'id': 'mw-content-text'}).find_all('a'):
                        if 'Category:Genre' in atag.attrs['href']:
                            album_genre += ('|' if album_genre else album_genre) + atag.text

            logging.info('GET Artist Album: ' + album)
            track_keys = albums[album].get('tracks')
            if track_keys:
                year = albums[album]['year']
                for song in track_keys:
                    resp = requests.get(base_url + track_keys[song])
                    lyric_soup = BS(resp.content)
                    lyrics_div = lyric_soup.find_all('div', {'class': 'lyricbox'})
                    lyrics_div = None if not lyrics_div else lyrics_div[0]
                    if lyrics_div:
                        for lyric in lyrics_div.childGenerator():
                            if isinstance(lyric, NavigableString) and lyric.strip():
                                lyric_dict = {
                                    'artist': artist,
                                    'lyric': lyric,
                                    'song': song,
                                    'year': year,
                                    'album': album,
                                    'id': uid.next(),
                                    'genre': genre,
                                    'album_genre': album_genre
                                }
                                lyrics_obj.append(lyric_dict)
            logging.info('GET Artist Album Successful: ' + album)
        return lyrics_obj
    except KeyboardInterrupt as ki:
        return lyrics_obj
