#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_kmeans_example(data, c1=(1,3), c2=(1,7), c3=(5,3), iterations=0):
    centroids = np.array([c1,c2,c3])
    if iterations == 0:
        plt.scatter(data[:, 0], data[:, 1], marker='s', c='gray', s=100, edgecolors='k')
        plt.scatter(centroids[:,0], centroids[:,1], facecolors=['green','red','blue'],
                    edgecolors='k', marker='x', s=250, linewidth=2)
        plt.title(f"K-Means Iteración {iterations}")
    else:
        kmeans = KMeans(n_clusters=3, init=centroids, n_init=1, max_iter=iterations).fit(data)
        plt.scatter(data[:, 0], data[:, 1], marker='s',  s=100, edgecolors='k',
                    c=[['green','red','blue'][l_] for l_ in kmeans.labels_])
        plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
                    facecolors=['green','red','blue'],
                    edgecolors='k', marker='x', s=250, linewidth=2)
        plt.title(f"K-Means Iteración {iterations}")
        # Step size of the mesh
        step_size = 0.01
        # Plot the boundaries
        x_min, x_max = min(data[:, 0]) - 1, max(data[:, 0]) + 1
        y_min, y_max = min(data[:, 1]) - 1, max(data[:, 1]) + 1
        x_values, y_values = np.meshgrid(np.arange(x_min, x_max,
        step_size), np.arange(y_min, y_max, step_size))
        # Predict labels for all points in the mesh
        predicted_labels = kmeans.predict(np.c_[x_values.ravel(),y_values.ravel()])
        predicted_labels = predicted_labels.reshape(x_values.shape)
        plt.imshow(predicted_labels, interpolation='nearest', alpha=0.5,
                   extent=(x_values.min(), x_values.max(), y_values.min(), y_values.max()),
                   cmap=ListedColormap(['green','red','blue']), aspect='auto', origin='lower')
    plt.grid(linestyle="dotted")
    plt.show()

