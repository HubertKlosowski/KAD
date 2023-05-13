import numpy as np
import matplotlib.pyplot as plt
import random
import os
from Zadanie3_pomoc import connect_arrays, getcolumn, find_duplicate

data = np.loadtxt("data.csv", delimiter=",", dtype=float)


def kmeans(array, k):
    array = [list(el) for el in array]
    rand = []
    centroids = []
    for i in range(k):
        x = random.randint(1, len(array) - 1)
        while not find_duplicate(rand, x):
            x = random.randint(1, len(array) - 1)
            if find_duplicate(rand, x):
                break
        rand.append(x)
        centroids.append(array[rand[i]])
    clusters = [[] for _ in range(k)]
    new_clusters = [[] for _ in range(k)]
    new_centroids = [[0.0 for _ in range(k)] for _ in range(k)]
    li = 0
    while not np.array_equal(centroids, new_centroids):
        for j in range(len(array)):
            distanses = []
            for u in range(k):
                dst = np.sqrt(((array[j][0] - centroids[u][0]) * (array[j][0] - centroids[u][0]))
                              + ((array[j][1] - centroids[u][1]) * (array[j][1] - centroids[u][1])))
                distanses.append(dst)
            minposition = distanses.index(min(distanses))
            clusters[minposition].append(array[j])
        for u in range(k):
            if len(clusters[u]) > 1:
                new_centroids[u] = np.round(np.mean(clusters[u], axis=0), 3)
            else:
                new_centroids[u] = centroids[u]
        if np.array_equal(centroids, new_centroids):
            new_clusters = clusters
            break
        else:
            clusters = [[] for _ in range(k)]
            centroids = new_centroids
            new_centroids = [[0.0 for _ in range(k)] for _ in range(k)]
            li += 1
    return new_clusters, centroids, li


def all_plots():
    tab = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    for o in range(2, 11):
        for i in range(6):
            result = kmeans(connect_arrays(getcolumn(data, tab[i][0]), getcolumn(data, tab[i][1])), o)
            colors = ["red", "blue", "green", "pink", "purple", "yellow", "grey", "orange", "brown", "white"]
            clusters = result[0]
            centroids = result[1]
            max_iter = result[2]
            for j, points in enumerate(clusters):
                x = [point[0] for point in points]
                y = [point[1] for point in points]
                plt.scatter(x, y, color=colors[j])
                plt.scatter(centroids[j][0], centroids[j][1], color=colors[j], marker="D", edgecolors="black")
            if i == 0:
                plt.xlabel("Długość działki kielicha (cm)")
                plt.ylabel("Szerokość działki kielicha (cm)")
            elif i == 1:
                plt.xlabel("Długość działki kielicha (cm)")
                plt.ylabel("Długość płatka (cm)")
            elif i == 2:
                plt.xlabel("Długość działki kielicha (cm)")
                plt.ylabel("Szerokość płatka (cm)")
            elif i == 3:
                plt.xlabel("Szerokość działki kielicha (cm)")
                plt.ylabel("Długość płatka (cm)")
            elif i == 4:
                plt.xlabel("Szerokość działki kielicha (cm)")
                plt.ylabel("Szerokość płatka (cm)")
            else:
                plt.xlabel("Długość płatka (cm)")
                plt.ylabel("Szerokość płatka (cm)")
            tmp = ['(%.1f,%.1f)' % (x[0], x[1]) for x in centroids]
            string = ','.join(tmp)
            plt.suptitle("Centroidy:\n" + string + "\nIlość iteracji = " + str(max_iter), fontsize=10)
            relative_path = "wykresy/kmeans"
            plt.savefig(os.path.join(relative_path, "kMeans_k_" + str(o) + "_i_" + str(i) + ".png"))
            plt.show()


all_plots()

