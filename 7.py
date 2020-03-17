import random
class Fractions(object):
    """docstring for Написать класс Дробное число со знаком (Fractions).
       Число должно быть представлено двумя полями: целая часть и дробная часть.
       Реализовать арифметические операции сложения, вычитания, умножения и
       операции сравнения. Проверить эти методы."""
    def __init__(self):
        self.wholePart = random.randint(-100,100)
        self.fractionPart = random.randint(0,100)
        self.numbers  = str(self.wholePart)+'.'+str(self.fractionPart)

    def to_double(self):
        return float(self.created_numbers())

    def sum(self, a, b):
        self.sum = (float(frac1.numbers) + float(frac2.numbers))
        return  self.sum

    def subtract(self, a, b):
        self.subtract = (float(frac1.numbers) - float(frac2.numbers))
        return self.subtract

    def multip(self, a, b):
        self.multip = (float(frac1.numbers) * float(frac2.numbers))
        return self.multip

    def compar(self, a, b):
        if frac1.numbers == frac2.numbers:
            return ' a == b'
        elif frac1.numbers < frac2.numbers:
            return 'a < b'
        else:
            return 'a > b'
            
frac1 = Fractions()
frac2 = Fractions()
print('число а = ',frac1.numbers)
print('число b = ',frac2.numbers)
print('a + b = ', frac1.sum(frac1, frac2))
print('a - b = ', frac1.subtract(frac1, frac2))
print('a * b = ', frac1.multip(frac1, frac2))
print('a vs b: ', frac1.compar(frac1, frac2))
