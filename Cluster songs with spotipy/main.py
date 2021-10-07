from get_track_info import get_track_info
from write_to_config import write_to_config

username = 'vvsoftware'
client_id = 'cd77ee1f13e74475bd5c63a793b13906'
client_secret = 'ef9621244a8c4a778347a5e61409613a'
redirect_uri = 'http://localhost:8080/'
filename = "config.json"
playlist_name = "Mooie liedjes"


def main():
    write_to_config(username, client_id, client_secret, redirect_uri, filename)
    tracks, names, uris, artists = get_track_info(username, playlist_name)


if __name__ == '__main__':
    main()
