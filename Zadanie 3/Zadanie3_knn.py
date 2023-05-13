import matplotlib.pyplot as plt
import numpy as np
import os
from Zadanie3_pomoc import connect_arrays, getcolumn

data_train = np.loadtxt("dane_train_test/data_train.csv", delimiter=",", dtype=float)
data_test = np.loadtxt("dane_train_test/data_test.csv", delimiter=",", dtype=float)


def knn(array, new_point, k):
    tab_dst = []
    L = []
    for point in array:
        L.append([point[0], point[1]])
        dst = np.sqrt(((point[0] - new_point[0]) * (point[0] - new_point[0]))
                      + ((point[1] - new_point[1]) * (point[1] - new_point[1])))
        tab_dst.append(dst)
    species = getcolumn(data_train, 4)
    for row in L:
        row.append(species.pop(0))
        row.append(tab_dst.pop(0))
    L = sorted(L, key=lambda x: x[3])
    L = L[:k]
    count = [0, 0, 0]
    for row in L:
        if row[2] == 0:
            count[0] += 1
        elif row[2] == 1:
            count[1] += 1
        else:
            count[2] += 1
        row.pop()
    return count.index(max(count))


def all_plots():
    tab = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    for o in range(1, 16):
        for i in range(6):
            point_shape = ["^", "s", "o"]
            colors = ["red", "blue", "green"]
            factual_species_test = [int(x) for x in getcolumn(data_test, 4)]
            factual_species_train = [int(x) for x in getcolumn(data_train, 4)]
            errors = [[0, 0, 0] for _ in range(3)]
            arr_test = connect_arrays(getcolumn(data_test, tab[i][0]), getcolumn(data_test, tab[i][1]))
            arr_train = connect_arrays(getcolumn(data_train, tab[i][0]), getcolumn(data_train, tab[i][1]))
            result_test = []
            j = 0
            for point in arr_test:
                result_test.append(knn(arr_train, point, o))
                if result_test[j] != factual_species_test[j]:
                    errors[factual_species_test[j]][result_test[j]] += 1
                j += 1
            j = 0
            for j in range(len(factual_species_train)):
                if factual_species_train[j] == 0:
                    plt.scatter(getcolumn(data_train, tab[i][0])[j], getcolumn(data_train, tab[i][1])[j], color=colors[0],
                                marker=point_shape[0])
                elif factual_species_train[j] == 1:
                    plt.scatter(getcolumn(data_train, tab[i][0])[j], getcolumn(data_train, tab[i][1])[j], color=colors[1],
                                marker=point_shape[1])
                else:
                    plt.scatter(getcolumn(data_train, tab[i][0])[j], getcolumn(data_train, tab[i][1])[j], color=colors[2],
                                marker=point_shape[2])
            j = 0
            for j in range(len(factual_species_test)):
                if result_test[j] == 0:
                    plt.scatter(getcolumn(data_test, tab[i][0])[j], getcolumn(data_test, tab[i][1])[j], edgecolors=colors[0],
                                marker=point_shape[0], color="white")
                elif result_test[j] == 1:
                    plt.scatter(getcolumn(data_test, tab[i][0])[j], getcolumn(data_test, tab[i][1])[j], edgecolors=colors[1],
                                marker=point_shape[1], color="white")
                else:
                    plt.scatter(getcolumn(data_test, tab[i][0])[j], getcolumn(data_test, tab[i][1])[j], edgecolors=colors[2],
                                marker=point_shape[2], color="white")
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
            plt.title("k = " + str(o))
            relative_path = "wykresy/knn"
            plt.savefig(os.path.join(relative_path, "kNN_k_" + str(o) + "_i_" + str(i) + ".png"))
            plt.show()


all_plots()
