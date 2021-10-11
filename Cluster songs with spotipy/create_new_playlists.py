import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pandas as pd
from math import ceil

scope = 'playlist-modify-public'


def load_config():  # Function to load the json file with the user credentials
    with open("config.json") as fp:
        file = json.load(fp)
        return file


user_config = load_config()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=user_config['client_id'],
                                               client_secret=user_config['client_secret'],
                                               redirect_uri=user_config['redirect_uri'],
                                               scope=scope))


def create_playlists(n_clusters, df):
    for cluster in range(n_clusters):
        result = sp.user_playlist_create(user_config['username'], 'cluster' + str(cluster), public=True,
                                         collaborative=False, description='')
        playlist_id = result['id']
        songs = list(df.loc[df['Clusters'] == cluster]['track_URI'])
        length = len(songs)
        for i in range(ceil((length/100))):
            last_i = len(range(ceil(length/100)))-1
            if i >= last_i:
                sp.playlist_add_items(playlist_id, songs[(i-1)*100:-1])
            else:
                sp.playlist_add_items(playlist_id, songs[(i-1)*100:i*100])
