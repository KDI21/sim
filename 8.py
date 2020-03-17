import random
# Написать класс Деньги для работы с денежными суммами.
# Число должно быть представлено двумя полями: одно для рублей и другое для копеек.
# Дробная часть (копейки) при выводе на экран должна быть отделена от целой
# части запятой. Реализовать сложение, вычитание, деление, умножение и операции
# сравнения. Проверить эти методы (выводить на экран результаты работы).

class Money(object):
    def created_cash(self):
        self.rubl = random.randint(1, 100)
        self.kop = random.randint(1, 100)
        return float(str(self.rubl)+'.'+str(self.kop))
    def sum (self, a, b):
        return (a + b)
    def subtract(self, a, b):
        return (a - b)
    def multip(self, a, b):
        return (a * b)
    def division(self, a, b):
        return (a / b)
    def compar(self, a, b):
        if a == b:
            return 'a = b'
        elif a < b:
            return 'a < b'
        else:
            return 'a > b'
money = Money()
a = money.created_cash()
print('транзакция а = ', a)
b = money.created_cash()
print('транзакция b = ', b)
print('a + b = ', money.sum(a, b))
print('a - b = ', money.subtract(a, b))
print('a * b = ', money.multip(a, b))
print('a / b = ', money.division(a, b))
print('a vs b: ', money.compar(a, b))
