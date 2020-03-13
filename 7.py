import random
class Fractions(object):
    """docstring for Написать класс Дробное число со знаком (Fractions).
       Число должно быть представлено двумя полями: целая часть и дробная часть.
       Реализовать арифметические операции сложения, вычитания, умножения и
       операции сравнения. Проверить эти методы."""

    def created_numbers(self):
        self.wholePart = random.randint(-100,100)
        self.fractionPart = random.randint(0,100)
        self.numbers  = str(self.wholePart)+'.'+str(self.fractionPart)
        return self.numbers
    def to_double(self):
        return float(self.created_numbers())
    def fold(self, a, b):
        return (float(a) + float(b))
    def subtract(self, a, b):
        return (float(a) - float(b))
    def multip(self, a, b):
        return (float(a) * float(b))
    def compar(self, a, b):
        if a == b:
            return ' a == b'
        elif a < b:
            return 'a < b'
        else:
            return 'a > b'
frac = Fractions()
a = frac.created_numbers()
print('число а = ',a)
b = frac.created_numbers()
print('число b = ',b)
print('a + b = ',frac.fold(a, b))
print('a - b = ', frac.subtract(a, b))
print('a * b = ', frac.multip(a,b))
print('a vs b: ', frac.compar(a, b))
