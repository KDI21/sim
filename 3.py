# Все элементы массива поделить на значение наибольшего элемента этого массива.
print('Задание 1')
mass = [2, 3, 5, 7, 8, 9, 23, 34, -33]

i = 0
while i < len(mass):
    b = mass[i] / max(mass)
    print(mass[i])
    print(b)
    i = i + 1
# Найти номер и значение первого положительного элемента массива
print('Задание 2')
mass = [-2, -3, -5, -7, 8, -9, 23, 34, -33]
n = len(mass)
i = 0
while i < n:
    if mass[i] > 0:
        print(i)
        print(mass[i])
        i = n
    i = i + 1

# Дан массив, содержащий положительные и отрицательные числа. Заменить все элементы
# массива на противоположные по знаку.
print('Задание 3')
mass = [-2, 3, -5, 7, 8, -9, 23, 34, -33]
print(mass)
n = len(mass)
i = 0
while i < n:
    mass[i] = -mass[i]
    i = i + 1
print(mass)
# В массиве найти минимальный и максимальный элементы, поменять их местами.
print('Задание 4')
mass = [-2, 3, -5, 7, 8, -9, 23, 34, -33]
print(mass)
a = mass.index(max(mass))
a1 = max(mass)
b = mass.index(min(mass))
b1 = min(mass)
mass[a] = b1
mass[b] = a1
print(mass)
# В одномерном массиве найти минимальный и максимальный элементы. Вычислить их разность.
print('Задание 5')
mass = [-2, 3, -5, 7, 8, -9, 23, 34, -33]
a1 = max(mass)
b1 = min(mass)
c = b1 - a1
print(c)
# Найти сумму тех элементов массива, которые одновременно имеют четные и отрицательные значения.
print('Задание 6')
mass = [-2, 3, 8, 13, -3, -4, 6, -7, -8, -3,-4, 4, 6, 8, 9]
i = 0
n = len(mass)
sum = 0
while i < n:
    if mass[i] < 0 and mass[i]%2 == 0:
        sum = sum +mass[i]
    i = i +1
print(sum)
# Из одномерного массива удалить все повторяющиеся элементы (дубликаты) так,
# чтобы каждое значение встречалось в массиве только один раз.
print('Задание 7')
mass = [-2, 3, 8, 13, -3, 4, 13, 3, -3, -2, -4, 6, -7, -8, -3,-4, 4, 6, 8, 9]
print(mass)
print(list(set(mass)))
