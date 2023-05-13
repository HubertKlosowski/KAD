import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.csv", delimiter=",", dtype=float)


def getCol(x):
    if x < 0 or x > 4:
        return 0
    kolumna = []
    for j in range(150):
        kolumna.append(data[j][x])
    return kolumna


def calSr(tab):
    sr = 0
    for i in range(len(tab)):
        sr += tab[i]
    sr /= len(tab)
    return sr


def calVar(tab):
    sx = 0
    for i in range(len(tab)):
        sx += (tab[i] - calSr(tab)) * (tab[i] - calSr(tab))
    sx /= len(tab)
    return sx


def calCoVar(tab1, tab2):
    if len(tab1) != len(tab2):
        return 0
    licznik = 0
    for i in range(len(tab1)):
        licznik += (tab1[i] - calSr(tab1)) * (tab2[i] - calSr(tab2))
    licznik /= len(tab1)
    return licznik


def calPearson(tab1, tab2):
    if len(tab1) != len(tab2):
        return 0
    mianownik = np.sqrt(calVar(tab1)) * np.sqrt(calVar(tab2))
    rxy = calCoVar(tab1, tab2) / mianownik
    return rxy


def calAB(tab1, tab2):
    a = calCoVar(tab1, tab2) / calVar(tab1)
    b = calSr(tab2) - (a * calSr(tab1))
    return a, b


def wykres_punktowy():
    tab = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    for i in range(6):
        plt.scatter(getCol(tab[i][0]), getCol(tab[i][1]))
        r = f'{calPearson(getCol(tab[i][0]), getCol(tab[i][1])):.2f}'
        a = f'{calAB(getCol(tab[i][0]), getCol(tab[i][1]))[0]:.1f}'
        b = f'{calAB(getCol(tab[i][0]), getCol(tab[i][1]))[1]:{"+"if round(calAB(getCol(tab[i][0]), getCol(tab[i][1]))[1], 1) else "-"}.1f}'
        plt.title("r = " + str(r) + "; y = " + str(a) + "x " + str(b))
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
        x = np.array(getCol(tab[i][0]))
        y = calAB(getCol(tab[i][0]), getCol(tab[i][1]))[0] * x + calAB(getCol(tab[i][0]), getCol(tab[i][1]))[1]
        plt.plot(x, y, '-r', label='y=' + str((calAB(getCol(tab[i][0]), getCol(tab[i][1]))[0] * x) + calAB(getCol(tab[i][0]), getCol(tab[i][1]))[1]))
        plt.show()


wykres_punktowy()
