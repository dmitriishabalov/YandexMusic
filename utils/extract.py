import os
from yandex_music import Client
import pandas as pd

CHART_ID = os.environ.get('CHART_ID')
TOKEN = os.environ.get('TOKEN')

client = Client(TOKEN).init()


def extract_data():
    chart = client.chart(CHART_ID).chart
    chart_df = pd.DataFrame()
    tracks = {'id': [], 'chart_position': [], 'title': [], 'available': [], 'artists': [], 'albums': [],
              'lyrics_available': [], 'real_id': [], 'cover_uri': [], 'duration_ms': []}

    for track_short in chart.tracks:
        track, chart = track_short.track, track_short.chart
        artists, albums = '', ''
        if track.artists:
            artists = ', '.join(artist.name for artist in track.artists)
        if track.albums:
            albums = ', '.join(album.title for album in track.albums)

        tracks['id'].append(track.id)
        tracks['chart_position'].append(chart.position)
        tracks['title'].append(track.title)
        tracks['available'].append(track.available)
        tracks['artists'].append(artists)
        tracks['albums'].append(albums)
        tracks['lyrics_available'].append(track.lyrics_available)
        tracks['real_id'].append(track.real_id)
        tracks['cover_uri'].append(track.cover_uri)
        tracks['duration_ms'].append(track.duration_ms)

        chart_df = chart_df.from_dict(tracks)
        chart_df = chart_df.set_index('chart_position')

        chart_df['lyrics_available'] = chart_df['lyrics_available'].fillna(False)
        chart_df['available'] = chart_df['lyrics_available'].fillna(False)

    return chart_df
