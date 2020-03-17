import random
import math
# Написать Класс Равнобочная трапеция, члены класса: координаты 4-х точек.
# Предусмотреть в классе конструктор и методы: проверка, является ли фигура
# равнобочной трапецией; вычисления и вывода сведений о фигуре: длины сторон,
# периметр, площадь. Продемонстрировать работу с классом: дано N трапеций,

# найти количество трапеций, у которых площадь больше средней площади.
class IsoscelesTrapezoid(object):

    def __init__(self):
        self.angles = []
        self.aX = random.randint(0, 16)
        self.bX = random.randint((int(self.aX)+3), 20)
        self.cX = random.randint((int(self.aX)+1), (int(self.bX)-2))
        self.dX = random.randint((int(self.cX)+1),(int(self.bX)-1))
        self.aY = random.randint(0, 9)
        self.bY = self.aY
        self.cY = random.randint((int(self.aY)+1), 10)
        self.dY = self.cY
        self.side_a = math.sqrt((int(self.cX) - int(self.aX)) ** 2 + (int(self.cY) - int(self.aY)) ** 2)
        self.side_c = math.sqrt((int(self.dX) - int(self.bX)) ** 2 + (int(self.dY) - int(self.bY)) ** 2)
        self.side_b = int(self.bX) - int(self.aX)
        self.side_d = int(self.dX) - int(self.cX)

    def creation_of_coordinates(self):
        # IsoscelesTrapezoid.__init__(self)
        self.angles.append('(' + str(self.aX) + ';' + str(self.aY) + ')' )
        self.angles.append('(' + str(self.bX) + ';' + str(self.bY) + ')' )
        self.angles.append('(' + str(self.cX) + ';' + str(self.cY) + ')' )
        self.angles.append('(' + str(self.dX) + ';' + str(self.dY) + ')' )
        return self.angles

    def isosceles_test(self):
        if self.side_a == self.side_c:
            return 'трапеция равнобедренная'
        else:
            return 'трапеция не равнобедренная'

    def perim(self):
        self.perim = (int(self.side_a) + int(self.side_b) + int(self.side_c) + int(self.side_d))
        return self.perim

    def area_1(self):
        self.h = int(self.cY) - int(self.aY)
        self.area  = (int(self.side_b) + int(self.side_d)) / 2 * self.h
        return self.area

    def more_than_average(self, n):
        """нанахождение количества трапеций, у которых площадь больше средней площади"""
        i = 1
        self.massive = [self.area]
        summa = self.area
        mass = []
        while i < n:
            IsoscelesTrapezoid.__init__(self)
            self.area = self.area_1()
            self.massive.append(self.area)
            summa = summa + self.area
            i = i + 1
        self.medium = summa / n
        a = 0
        print(self.massive)
        while a < n:
            if self.massive[a] > self.medium:
                mass.append(self.massive[a])
                pass
            a = a + 1
        self.quantity = len(mass)


I = IsoscelesTrapezoid()
print('координаты трапеции', I.creation_of_coordinates())
print(I.isosceles_test())
print('нижние основание = ', I.side_b,' верхние основание = ', I.side_d,' левоя сторона = ', I.side_a,' правая сторона = ', I.side_c)
print('периметр: ', I.perim())
print("площать: ", I.area_1())
n = int(input('сколько трапеций: '))
I.more_than_average(n)
print(I.massive, 'средние зничение площади: ', I.medium, 'больше средней прощади', I.quantity)
