import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer


def dimensionality_reduction(df):
    non_features = ['name', 'artist', 'track_URI', 'playlist'] # Columns that need dropping
    track_info = df[non_features]
    df_x = df.drop(columns=non_features)
    scaler = StandardScaler()
    X_std = scaler.fit_transform(df_x)
    pca = PCA().fit(X_std)
    evr = pca.explained_variance_ratio_

    n_comps = 0
    for i, exp_var in enumerate(evr.cumsum()):
        if exp_var >= 0.8:
            n_comps = i + 1
            break
    pca = PCA(n_components=n_comps).fit(X_std)
    scores_pca = pca.transform(X_std)
    return scores_pca


def k_means_clustering(scores_pca):
    visualizer = KElbowVisualizer(KMeans(init='k-means++', random_state=42), k=(1, 21), timings=False)
    visualizer.fit(scores_pca)
    optimal_k = visualizer.elbow_value_
    k_means_pca = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
    k_means_pca.fit(scores_pca)
    return k_means_pca, optimal_k
