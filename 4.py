# Создайте функцию, печатающую в консоли слово Hello и программу, которая с ее
# помощью напечатает слово Hello 10 раз.
print('Задание 1')
def hello():
    print('Hello')
i = 0
while i < 10:
    hello()
    i = i + 1

# Создайте функцию, возводящую число в целую степень. Число и степень должны быть,
# естественно, параметрами.
print('Задание 2')
a = int(input('Ведите число: '))
b = int(input('Ведите степень: '))
def step(a,b):
    i = 0
    c = 1
    while i < b:
        c = c * a
        i = i + 1
    print(c)
step(a,b)

# Создайте функцию, возвращающую индекс максимального элемента части массива.
# Часть задавайте диапазоном индексов (с какого по какой).
print('Задание 3')
a = int(input('откуда: '))
b = int(input('докуда: '))
mass = [3, 4, 43, 56 ,6, 8, 44, 67, 55, 45, 68, 3, 5]
def max_el(mass,min,max):
    i = min - 1
    c = 0
    while i < max:
        if c < mass[i]:
            c = mass[i]
        i = i + 1
    d = mass.index(c)
    print(d,' ',c)
max_el(mass,a,b)

# Сгенерировать десять массивов из случайных чисел. Вывести их и сумму их
# элементов на экран. Найти среди них один с максимальной суммой элементов.
# Указать какой он по счету, повторно вывести этот массив и сумму его элементов.
# Заполнение массива и подсчет суммы его элементов оформить в виде отдельной функции.
print('Задание 4')
import random
def gen_mass():
    i = 0
    mass = []
    sum = 0
    while i < 15 :
        mass.append(random.randint(-100,100))
        sum = sum + mass[i]
        i = i + 1

    mass.append(sum)
    return mass
def max_sum():
    i = 0
    mas_max = []
    sum_max = 0
    while i < 10:
        mass = gen_mass()
        if mass[-1] > sum_max:
            n = i
            sum_max = mass[-1]
            mas_max = mass
        i = i + 1
        summ = mass[-1]
        mass.pop()
        print('Massiv',i,': ',mass,' Summa: ', summ)
    mas_max.pop()
    print('Massiv',n,': ', mas_max, 'Max_Summa: ', sum_max)
max_sum()
