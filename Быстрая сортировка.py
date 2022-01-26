import random


def quick_sort(a):
    if len(a) > 1: # Если массив a по кол-ву значений больше чем 1
        x = a[random.randint(0, len(a)-1)] # случайное пороговое значение (для разделения на малые и большие)
        low = [u for u in a if u < x] # малая группа
        eq = [u for u in a if u == x] # центральная
        hi = [u for u in a if u > x]  # большая группа
        a = quick_sort(low) + eq + quick_sort(hi)  # (функция quick_sort сортирует группы), складываем списки

    return a


a = [9, 5, -3, 4, 7, 8, -7]
a = quick_sort(a)

print(a)
