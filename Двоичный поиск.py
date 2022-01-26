from random import randint
import datetime


def find_num(array, key):
    """
    Комментарий для теста
    :param array:
    :param key:
    :return:
    """


def binary_search(array, key):
    lower_bound = 0             #верхняя граница
    upper_bound = len(array) -1  #нижня граница (длинна нашего массива)

    while lower_bound <= upper_bound: #если верхняя граница меньше нижней retiurn -1 (возвращаем -1, те. элемент который мы ищем нет в массиве)
        center = (lower_bound + upper_bound) // 2 # ищем центр массива (берем только целую часть от деления)

        if array[center] == key:
            return center
        elif array[center] > key:
            upper_bound = center - 1
        elif array [center] < key:
            lower_bound += center + 1

    return -1

x = [randint(0, 10) for a in range (10)]
x = sorted(x)
print("Array created")
print("Array sorted")
print(x)

start = datetime.datetime.now() # Время на нашем компьютере сейчас
print(find_num(x, 67))
print(datetime.datetime.now() - start) # Время на компьютере сейчас - время старта
