import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt("data.csv", delimiter=",", dtype=float)


def calculate_min_maks(tab, tmp):
    if tmp == 0:
        minimum = tab[0]
        for i in range(len(tab)):
            if minimum > tab[i]:
                minimum = tab[i]
        return minimum

    elif tmp == 1:
        maks = tab[0]
        for i in range(len(tab)):
            if maks < tab[i]:
                maks = tab[i]
        return maks
    else:
        return 0


def calculate_srednia(tab):
    suma = 0
    for i in range(len(tab)):
        suma += tab[i]
    return suma / len(tab)


def calculate_kwantyl(tab, tmp):
    if len(tab) < 3:
        return 0
    tab.sort()
    tab1 = []
    tab2 = []
    if len(tab) % 2 == 0:
        if tmp == 0.5:
            return (tab[int(len(tab) / 2)] + tab[int(len(tab) / 2) - 1]) / 2
        elif tmp == 0.25:
            for i in range(int(len(tab) / 2)):
                tab1.append(tab[i])
            if len(tab1) % 2 == 0:
                return (tab1[int(len(tab1) / 2)] + tab1[int(len(tab1) / 2) - 1]) / 2
            else:
                return tab1[int(len(tab1) / 2) - 1]
        elif tmp == 0.75:
            for i in range(int(len(tab) / 2), len(tab)):
                tab2.append(tab[i])
            if len(tab2) % 2 == 0:
                return (tab2[int(len(tab2) / 2)] + tab2[int(len(tab2) / 2) - 1]) / 2
            else:
                return tab2[int(len(tab2) / 2) - 1]
        else:
            return 0

    else:
        if tmp == 0.5:
            return tab[int((len(tab) - 1) / 2)]
        elif tmp == 0.25:
            for i in range(int((len(tab) - 1) / 2)):
                tab1.append(tab[i])
            if len(tab1) % 2 == 0:
                return (tab1[int(len(tab1) / 2)] + tab1[int(len(tab1) / 2) - 1]) / 2
            else:
                return tab1[int(len(tab1) / 2) - 1]
        elif tmp == 0.75:
            for i in range(int((len(tab) + 1) / 2), len(tab)):
                tab2.append(tab[i])
            if len(tab2) % 2 == 0:
                return (tab2[int(len(tab2) / 2)] + tab2[int(len(tab2) / 2) - 1]) / 2
            else:
                return tab2[int(len(tab2) / 2) - 1]
        else:
            return 0


def calculate_odchylenie_dla_proby(tab):
    sum_i = 0
    for i in range(len(tab)):
        sum_i += ((tab[i] - calculate_srednia(tab)) * (tab[i] - calculate_srednia(tab)))
    sum_i /= (len(tab) - 1)
    return math.sqrt(sum_i)


def liczebnosc_udzial_procentowy():
    """
        tab[0] = liczebnosc setosa
        tab[1] = liczebnosc versicolor
        tab[2] = liczebnosc virginica
    """
    tab = [0, 0, 0]
    for i in range(int(data.size / 5)):
        if data[i][4] == 0:
            tab[0] += 1
        elif data[i][4] == 1:
            tab[1] += 1
        else:
            tab[2] += 1
    for i in range(3):
        tab.append(((tab[i] / 150) * 100).__round__(1))
    return tab


def srednia_mediana_kwantyle_odchylenie_standardowe():
    """
        (0) - min
        (1) - srednia arytmetyczna
        (2) - odchylenie standardowe
        (3) - mediana
        (4) - kwartyl Q1
        (5) - kwantyl Q3
        (6) - maks
    """
    tab = []
    wyniki = [[], [], [], []]
    for j in range(4):
        for i in range(int(data.size / 5)):
            tab.append(data[i][j])
        wyniki[j].append(calculate_min_maks(tab, 0))
        wyniki[j].append(calculate_srednia(tab).__round__(2))
        wyniki[j].append(calculate_odchylenie_dla_proby(tab).__round__(2))
        wyniki[j].append(calculate_kwantyl(tab, 0.5))
        wyniki[j].append(calculate_kwantyl(tab, 0.25))
        wyniki[j].append(calculate_kwantyl(tab, 0.75))
        wyniki[j].append(calculate_min_maks(tab, 1))
        tab.clear()
    return wyniki


def histogram_lacznie_gatunki():
    tab = []
    for i in range(4):
        for j in range(int(data.size / 5)):
            tab.append(data[j][i])

        if i == 0:
            plt.hist(tab, bins=[4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0], edgecolor='black')
            plt.xlabel('Długość (cm)')
            plt.ylabel('Liczebność')
            plt.title('Długość działki kielicha')
            plt.show()
        elif i == 1:
            plt.hist(tab, bins=[2.0, 2.5, 3.0, 3.5, 4.0, 4.5], edgecolor='black')
            plt.xlabel('Szerokość (cm)')
            plt.ylabel('Liczebność')
            plt.title('Szerokość działki kielicha')
            plt.show()
        elif i == 2:
            plt.hist(tab, bins=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0], edgecolor='black')
            plt.xlabel('Długość (cm)')
            plt.ylabel('Liczebność')
            plt.title('Długość płatka')
            plt.show()
        else:
            plt.hist(tab, bins=[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], edgecolor='black')
            plt.xlabel('Szerokość (cm)')
            plt.ylabel('Liczebność')
            plt.title('Szerokość płatka')
            plt.show()
        tab.clear()


def histogram_pudelka_osobno_gatunki():
    colors = ['green', 'blue', 'orange']
    tab = [[], [], []]
    for j in range(4):
        for i in range(int(data.size / 5)):
            if data[i][4] == 0:
                tab[0].append(data[i][j])
            elif data[i][4] == 1:
                tab[1].append(data[i][j])
            else:
                tab[2].append(data[i][j])

        if j == 0:
            plt.hist(tab, bins=[4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0], edgecolor='black', color=colors)
            plt.xlabel('Długość (cm)')
            plt.title('Długość działki kielicha')
            plt.legend(['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Liczebność')
            plt.show()
            plt.clf()
            plt.boxplot(tab)
            plt.title('Długość działki kielicha')
            plt.xticks([1, 2, 3], ['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Długość (cm)')
            plt.xlabel('Gatunek')
            plt.show()
        elif j == 1:
            plt.hist(tab, bins=[2, 2.5, 3, 3.5, 4, 4.5], edgecolor='black', color=colors)
            plt.xlabel('Szerokość (cm)')
            plt.title('Szerokość działki kielicha')
            plt.legend(['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Liczebność')
            plt.show()
            plt.clf()
            plt.boxplot(tab)
            plt.title('Szerokość działki kielicha')
            plt.xticks([1, 2, 3], ['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Szerokość (cm)')
            plt.xlabel('Gatunek')
            plt.show()
        elif j == 2:
            plt.hist(tab, bins=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0], edgecolor='black', color=colors)
            plt.xlabel('Długość (cm)')
            plt.title('Długość płatka')
            plt.legend(['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Liczebność')
            plt.show()
            plt.clf()
            plt.boxplot(tab)
            plt.title('Długość płatka')
            plt.xticks([1, 2, 3], ['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Długość (cm)')
            plt.xlabel('Gatunek')
            plt.show()
        else:
            plt.hist(tab, bins=[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], edgecolor='black', color=colors)
            plt.xlabel('Szerokość (cm)')
            plt.title('Szerokość płatka')
            plt.legend(['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Liczebność')
            plt.show()
            plt.clf()
            plt.boxplot(tab)
            plt.title('Szerokość płatka')
            plt.xticks([1, 2, 3], ['setosa', 'versicolor', 'virginica'])
            plt.ylabel('Szerokość (cm)')
            plt.xlabel('Gatunek')
            plt.show()

        for i in range(3):
            tab[i].clear()


print(liczebnosc_udzial_procentowy())
print(srednia_mediana_kwantyle_odchylenie_standardowe())
histogram_lacznie_gatunki()
histogram_pudelka_osobno_gatunki()
