#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Факториал числа представляет собой произведение всех натуральных чисел от 1 до
# этого числа включительно
print('Задание 1')
a = int(input('Ведите число: '))
i =1
b = 1
while i <= a:
    b = b * i
    i = i + 1
print(b)
# Вывести на экран ряд чисел Фибоначчи, состоящий из n элементов.
print('Задание 2')
fib1 = 0
fib2 = 1
n = int(input("Номер элемента ряда Фибоначчи: "))
i = 0
print(fib1)
print(fib2)
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    print(fib2)

# Возвести чилсо в степень с помощью цикла и операции умножения
print('Задание 3')
a = int(input('Число: '))
n = int(input('Степень: '))
i = 1
b = a
while i < n:
    b = b * a
    i = i + 1
print('Число ', a, 'в степени ', n, 'равно ', b)
# С помощью оператора while напишите программу определения суммы всех нечетных
# чисел в диапазоне от 1 до 99 включительно.
print('Задание 4')
i = 1
sum = 0
while i < 100:
    if i % 2 == 1:
        sum = sum + i
    i = i + 1
print(sum)
# с помощью оператора while напишите программу вывода всех четных чисел в
# диапазоне от 2 до 100 включительно.

print('Задание 5')
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1
# Имеется кусок ткани длинной M метров. От него последовательно отрезаются куски
# равной длины. Все данные по использованию ткани заносятся в компьютер.
# Компьютер должен выдать сообщение о том, что материала не хватает,
# если будет затребован кусок ткани больше длины, чем имеется.
print('Задание 6')
all = int(input('сколько всего ткани: '))
i = 1
while i != 0 :
    a = int(input('сколько отрезать: '))
    if all < a:
        print('недостаточно ткани')
        i = 0
    else:
        all = all - a
        print('осталось: ',all)
        i = all
