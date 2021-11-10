import spotipy
from spotipy.oauth2 import SpotifyOAuth

#following information should be received by log in of user
username = "simonhuesgen"
client_id = "1bddac7ecedc42bb823efd6035dd6beb"
client_secret = "b4b500e1cecc4cdc9cfa5ee38b97facb"
redirect_uri = "http://localhost:8080/"

scope = 'playlist-modify-public'
token = SpotifyOAuth(client_id,client_secret,redirect_uri,scope=scope,username=username)
sp = spotipy.Spotify(auth_manager=token)

recommended_songs = []
#whenever a song is recommended to the user based on mood/ clusters or liked songs, the song id/url/uri should
#be saved in this list (recommended_songs.append(result["tracks"]["items"][0]["uri"])) and at the end of the chatbot
#interaction the user can be asked if they want a playlist based on their chatbot interaction


def make_recommended_playlist(name = "Recommendation Playlist"):
    new_playlist = sp.user_playlist_create(username, name, public=True,description="This playlist was created by the GroupyGrouperson chatbot")
    sp.playlist_add_items(new_playlist["id"],recommended_songs)

make_recommended_playlist()
