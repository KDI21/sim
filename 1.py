#!/usr/bin/env python
# -*- coding: utf-8 -*-


print('Задание 1')
a = int(input('Ведите первое число: '))
b = int(input('Ведите второе число: '))

if a > b:
    c = a + b
    print(c, 'ЗАДАЧА РЕШЕНА')
else:
    c = a * b
    print(c, 'ЗАДАЧА РЕШЕНА')


print('Задание 2')
a = int(input('Ваш возраст: '))
if 25 <= a <41:
    print('Вы нам подходите')
else:
    print('Вы нам не подходите')

print('Задание 3')
a = int(input('Видите чесло: '))
if a % 2 == 0:
    print('Число чётное')
else:
    print('Число не чётное')

print('Задание 4')
a = int(input('Видите чесло: '))
if 27 < a < 31:
    print('попал')
elif 30 < a:
    print('перелёт')
elif 0 <= a <28:
    print('недолёт')
else:
    print('не бей по своим')

print('Задание 5')
a = str(input('Ведите номер билета: '))
if len(a) <= 5:
    print('номер слишком короткий')
else:
    b = int(a[0]) + int(a[1]) + int(a[2])
    c = int(a[-1]) + int(a[-2]) + int(a[-3])
    print(b,'  ',c)
    if b == c:
        print('Номер счасливый')
    else:
        print('номер не счасливый')




print('Задание 6')
a = int(input('Ведите сумму покупки: '))
if a >1000:
    print(a*0.85)
else:
    print('Скидка не предостовляется')

print('Задание 7')
import math
a = int(input('Ведите площать круга: '))
b = int(input('Ведите площать квадрата: '))
if math.sqrt(b) > 2 * math.sqrt(a / 3.14):
    print('Круг поместится в квадрат')
else:
    print('Круг не поместится в квадрат')


print('Задание 8')
a = float(input('Ведите число: '))
if -5 < a > 3:
    print('Число не принадлежит интервалу (-5;3)')
else:
    print('Число  принадлежит интервалу (-5;3)')

print('Задание 9')
a = int(input('Видите длину стороны a: '))
b = int(input('Видите длину стороны b: '))
c = int(input('Видите длину стороны c: '))
if (a == b or a == c or b == c):
    print('Триугольник равнобедренный')
else:
    print('Триугольник не  равнобедренный')
