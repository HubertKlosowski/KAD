def getcolumn(arr, x):
    if x < 0 or x > 4:
        return 0
    kolumna = []
    for j in range(int(arr.size / 5)):
        kolumna.append(arr[j][x])
    return kolumna


def connect_arrays(arr1, arr2):
    return list(zip(arr1, arr2))


def find_duplicate(array, number):
    for num in array:
        if num == number:
            return False
    return True
