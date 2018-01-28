Welcome to the Cypher. Blog post [here](https://tmthyjames.github.io/tools/Cypher/)

=======================

Easily get music lyrics


To install, use `pip`:

`pip install thecypher`

Example:

```python
>>> import thecypher as cy
>>> coasts = cy.get_lyrics('coasts')
>>> coasts[0]
{'album': 'Coasts (2016)',
 'artist': 'coasts',
 'genre': 'Indie_Pop',
 'id': 0,
 'lyric': 'We fell in love',
 'song': 'Oceans',
 'year': '2016'}
```

Convert it to a pandas DataFrame like so:

```python
>>> import pandas as pd
>>> coasts_df = pd.DataFrame(coasts)
>>> coasts_df.head()
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right">
      <th></th>
      <th>album</th>
      <th>artist</th>
      <th>genre</th>
      <th>id</th>
      <th>lyric</th>
      <th>song</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Coasts (2016)</td>
      <td>coasts</td>
      <td>Indie_Pop</td>
      <td>0</td>
      <td>We fell in love</td>
      <td>Oceans</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Coasts (2016)</td>
      <td>coasts</td>
      <td>Indie_Pop</td>
      <td>1</td>
      <td>Right by the ocean</td>
      <td>Oceans</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Coasts (2016)</td>
      <td>coasts</td>
      <td>Indie_Pop</td>
      <td>2</td>
      <td>Made all our plans</td>
      <td>Oceans</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Coasts (2016)</td>
      <td>coasts</td>
      <td>Indie_Pop</td>
      <td>3</td>
      <td>Down on the sand</td>
      <td>Oceans</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Coasts (2016)</td>
      <td>coasts</td>
      <td>Indie_Pop</td>
      <td>4</td>
      <td>And from the tips of your fingers</td>
      <td>Oceans</td>
      <td>2016</td>
    </tr>
  </tbody>
</table>



