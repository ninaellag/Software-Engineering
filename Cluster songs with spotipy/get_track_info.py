import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pandas as pd

scope = 'playlist-read-private'


def load_config():  # Function to load the json file with the user credentials
    with open("config.json") as fp:
        file = json.load(fp)
        return file


user_config = load_config()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=user_config['client_id'],
                                               client_secret=user_config['client_secret'],
                                               redirect_uri=user_config['redirect_uri'],
                                               scope=scope))


def fetch_playlist_id(playlists, playlist_name):
    playlist_id = 0
    for playlist in playlists:
        if playlist['name'].lower() == playlist_name.lower():
            playlist_id = playlist['id']
            return playlist_id
    return 0


def get_playlist_id(username, playlist_name):   # Get playlist id by entering name of playlist
    offset_playlists = 0
    playlists = []
    while True:
        results = sp.user_playlists(username, limit=50, offset=offset_playlists)
        fifty = results['items']
        playlists.append(fifty)
        if results['next'] is not None:
            offset_playlists += 50
        else:
            break

    playlists = playlists[0]
    playlist_id = fetch_playlist_id(playlists, playlist_name)
    return playlist_id


def get_track_info(username, playlist_name): # Get playlist tracks by entering playlist ID
    playlist_id = get_playlist_id(username, playlist_name)
    offset = 0
    tracks, names, uris, artists = [], [], [], []
    while True:
        results = sp.user_playlist_tracks(user=user_config['username'], playlist_id=playlist_id, limit=100,
                                          offset=offset)
        tracks += results['items']
        if results['next'] is not None:
            offset += 100
        else:
            break

    names, uris, artists = fetch_track_info(tracks)
    return playlist_name, names, uris, artists


def fetch_track_info(tracks):
    names, uris, artists = [], [], []
    for track in tracks:
        if track['track'] is not None:
            names.append(track['track']['name'])
            uris.append(track['track']['uri'])
            artists.append(track['track']['artists'][0]['name'])
    return names, artists, uris


def get_features_for_playlist(username, playlist_name):
    df = pd.DataFrame(columns=['name', 'artist', 'track_URI', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'playlist'])
    playlist_name, names, artists, uris = get_track_info(username, playlist_name)

    for name, artist, track_uri in zip(names, artists, uris):

        audio_features = sp.audio_features(track_uri)

        if audio_features[0] is not None:
            feature_subset = [audio_features[0][col] for col in df.columns if col not in ["name", "artist", "track_URI", "playlist"]]

            row = [name, artist, track_uri, *feature_subset, playlist_name]
            df.loc[len(df.index)] = row
    return df
