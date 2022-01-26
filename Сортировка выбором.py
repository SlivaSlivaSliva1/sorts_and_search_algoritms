import datetime
from random import randint

x = [-4, 0, 7, -1, 10, 50, -65, -4, 5, 7, 10, 3, 6, 2]
N=len(x)               #Число элементов в списке
for i in range (N-1):
  m = x[i]                #Минимальное значение
  p = i                   #Индекс минимального значения
  for j in range(i+1, N): #Поиск минимального значения
    if m > x[j]:
      m = x[j]
      p = j

if p !=i:    #Обмен значениями
  t = x[i]
  x[i] = x[p]
  x[p] = t

print(x)

