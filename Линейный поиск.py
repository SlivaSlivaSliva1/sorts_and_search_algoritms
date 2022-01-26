import datetime
from random import randint

x = [randint(-100, 100) for a in range(-100, 100)]
#Генератор рандомных чисел

def find_num(array, key): #Через эту функцию передаем массив и ключ который ищем
    for i in range(len(array)):
        if array[i] ==key:
             return i

    return -1

start = datetime.datetime.now() # Время на нашем компьютере сейчас
print(find_num(x, -50))
print(datetime.datetime.now() - start) # Время на компьютере сейчас - время старта
#Выдаем индекс числа в массиве x
# O(n) - Линейный поиск