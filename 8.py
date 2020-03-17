import random
# Написать класс Деньги для работы с денежными суммами.
# Число должно быть представлено двумя полями: одно для рублей и другое для копеек.
# Дробная часть (копейки) при выводе на экран должна быть отделена от целой
# части запятой. Реализовать сложение, вычитание, деление, умножение и операции
# сравнения. Проверить эти методы (выводить на экран результаты работы).

class Money(object):
    def __init__(self):
        self.rubl = random.randint(1, 100)
        self.kop = random.randint(1, 100)
        self.cash = float(str(self.rubl)+'.'+str(self.kop))

    def sum (self, a, b):
        self.sum = (money1.cash + money2.cash)
        return self.sum

    def subtract(self, a, b):
        self.subtract =  (money1.cash - money2.cash)
        return self.subtract

    def multip(self, a, b):
        self.multip =  (money1.cash * money2.cash)
        return self.multip

    def division(self, a, b):
        self.division =  (money1.cash / money2.cash)
        return self.division

    def compar(self, a, b):
        if money1.cash == money2.cash:
            return 'a = b'
        elif money1.cash < money2.cash:
            return 'a < b'
        else:
            return 'a > b'
money1 = Money()
money2 = Money()
print('транзакция b = ', money2.cash)
print('транзакция а = ', money1.cash)
print('a + b = ', money1.sum(money1, money2))
print('a - b = ', money1.subtract(money1, money2))
print('a * b = ', money1.multip(money1, money2))
print('a / b = ', money1.division(money1, money2))
print('a vs b: ', money1.compar(money1, money2))
