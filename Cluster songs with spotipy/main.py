from get_track_info import get_features_for_playlist
from write_to_config import write_to_config
from pca_and_clustering import dimensionality_reduction, k_means_clustering
from create_new_playlists import create_playlists
import pandas as pd
import json


username = 'vvsoftware'
client_id = 'cd77ee1f13e74475bd5c63a793b13906'
client_secret = 'ef9621244a8c4a778347a5e61409613a'
redirect_uri = 'http://localhost:8080/'
filename = "config.json"
playlist_name = "Monica"


def main():
    write_to_config(username, client_id, client_secret, redirect_uri, filename)

    df = get_features_for_playlist(username, playlist_name)

    scores_pca = dimensionality_reduction(df)

    k_means_pca, n_clusters = k_means_clustering(scores_pca)

    df['Clusters'] = k_means_pca.labels_

    create_playlists(n_clusters, df)

    df.sort_values(by=['Clusters'], ascending=True)
    df.to_csv("clustered_songs.csv")


if __name__ == '__main__':
    main()
