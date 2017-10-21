import re
import requests
from bs4 import BeautifulSoup as BS
from bs4.element import NavigableString

def get_lyrics(artist):
    base_url = 'http://lyrics.wikia.com'
    url_ext = '/wiki/'
    # artist = 'Kendrick_Lamar'
    req = requests.get(base_url + url_ext + artist)
    resp = BS(req.content, 'html')
    
    albums = {}
    nodes = resp.find_all('div', {'id': 'mw-content-text'})[0].find_all()#'ol', recursive=False)
    for node in nodes:
        if node.name == 'h2':
            if node.find_all('span'):
                a_tag = node.find_all('a')
                title = 'Misc (0000)' if not a_tag else a_tag[0].text
                year_search = re.search('([0-9]{4})', title)
                album_year = None if not year_search else year_search.group(0)
    #             if not title:    
    #                 continue
                albums[title] = {}
                albums[title]['year'] = album_year
        if node.name == 'ol':
            for song in node:
                track_node = song.find_all('a')[0]
                track_name = track_node.text
                track_href = track_node.get('href')
                if 'tracks' not in albums[title]:
                    albums[title]['tracks'] = {}
                albums[title]['tracks'][track_name] = track_href

    album_keys = albums.keys()
    lyrics_obj = []
    for album in album_keys:
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
                                'album': album
                            }
                            lyrics_obj.append(lyric_dict)
                else:
                    print song, album, base_url + track_keys[song]
    return lyrics_obj