import math
# Построить систему классов для описания плоских геометрических фигур: круга,
# квадрата, прямоугольника. Предусмотреть методы для создания объектов,
# перемещения на плоскости.
class Square(object):
    """описание квадрата"""
    def __init__(self, ldX = 0, ldY = 0, length = 2):
        super(Square, self).__init__()
        self.ldX = ldX
        self.ldY = ldY
        self.length = length
        self.angles = []

    def area_sqr (self):
        """ Определение площади"""
        return self.length ^ 2

    def perim_sqr(self):
        """Определение периметра"""
        return self.length*4

    def diagonal_sqr(self):
        """Определение диагонали"""
        return math.sqrt(self.length * self.length * 2)

    def angle_coordinates(self):
        """Определение координат углов квадрата. Координаты углов начинают
           определяться с левого нижнего, против часовой стрелки """
        self.angles.append('(' + str(self.ldX) + ';' + str(self.ldY) + ')' )
        self.angles.append('(' + str(self.ldX + self.length)  + ';' + str(self.ldY) + ')' )
        self.angles.append('(' + str(self.ldX + self.length) + ';' + str(self.ldY + self.length) + ')' )
        self.angles.append('(' + str(self.ldX) + ';' + str(self.ldY + self.length) + ')' )
        return self.angles

    def moveTo(self, X, Y):
        """перемешение квадрата в плоскости"""
        self.ldX = X
        self.ldY = Y
        self.angles.clear()
        return self.angle_coordinates()

class Rectangle(object):
    """docstring for Rectangle."""

    def __init__(self, ldX, ldY, length_A, length_B):
        super(Rectangle, self).__init__()
        self.ldX = ldX
        self.ldY = ldY
        self.length_A = length_A
        self.length_B = length_B
        self.angles = []

    def area_rec(self):
        """ Определение площади"""
        return   self.length_A * self.length_B

    def perim_rec(self):
        """Определение периметра"""
        return (self.length_A + self.length_B) * 2

    def diagonal_rec(self):
        """Определение диагонали"""
        return math.sqrt(self.length_A * self.length_A + self.length_B * self.length_B)

    def angle_coordinates(self):
        """Определение координат углов прямоугольника. Координаты углов начинают
           определяться с левого нижнего, против часовой стрелки """
        self.angles.append('(' + str(self.ldX) + ';' + str(self.ldY) + ')' )
        self.angles.append('(' + str(self.ldX + self.length_A)  + ';' + str(self.ldY) + ')' )
        self.angles.append('(' + str(self.ldX + self.length_A) + ';' + str(self.ldY + self.length_B) + ')' )
        self.angles.append('(' + str(self.ldX) + ';' + str(self.ldY + self.length_B) + ')' )
        return self.angles

    def moveTo(self, X, Y):
        """перемешение прямоугольника в плоскости"""
        self.ldX = X
        self.ldY = Y
        self.angles.clear()
        return self.angle_coordinates()

class Circle(object):
    """docstring for Circle."""

    def __init__(self, x, y, r ):
        super(Circle, self).__init__()
        self.X = x
        self.Y = y
        self.R = r

    def area_crl(self):
        """Определение площади"""
        return 3.14 * self.R * self.R

    def perim_crl(self):
        """Определение периметра"""
        return 2 * 3.14 * self.R

    def moveTo(self, x, y):
        self.X = x
        self.Y = y
        return '(' + str(self.X)+';'+ str(self.Y)+')'

# для работы с квадратом
ldX = int(input('ведите координату Х для левого нижего угла квадрата: '))
ldY = int(input('ведите координату Y для левого нижего угла квадрата: '))
length = int(input('ведите длину ребра квадрата: '))
square = Square(ldX, ldY, length)
print('площать кадрата: ', square.area_sqr())
print('периметр квадрата: ', square.perim_sqr())
print('Диагональ квадрата: ',square.diagonal_sqr())
print('квадрат находиться по этим координатам:', square.angle_coordinates())
X = int(input('ведите координату Х левого нижего угла для перемешения квадрата: '))
Y = int(input('ведите координату Y  левого нижего угла для перемешения квадрата: '))
print('квадрат переместился и находиться по этим координатам: ', square.moveTo(X,Y))

# # для работы с прямоугольником
ldX = int(input('ведите координату Х для левого нижего угла прямоугольника: '))
ldY = int(input('ведите координату Y для левого нижего угла прямоугольника: '))
length_A = int(input('ведите длину  прямоугольника: '))
length_B = int(input('ведите ширину  прямоугольника: '))
rectangle = Rectangle(ldX, ldY, length_A, length_B)
print('площать прямоугольника: ', rectangle.area_rec())
print('периметр прямоугольника: ', rectangle.perim_rec())
print('Диагональ прямоугольника: ', rectangle.diagonal_rec())
print('прямоугольник находиться по этим координатам: ',rectangle.angle_coordinates())
X = int(input('ведите координату Х левого нижего угла для перемешения прямоугольника: '))
Y = int(input('ведите координату Y  левого нижего угла для перемешения прямоугольника: '))
print('прямоугольник переместился и находиться по этим координатам: ', rectangle.moveTo(X, Y))

# для работы с кругом
x = int(input('ведите  координату Х для центра круга: '))
y = int(input('ведите  координату Y для центра круга: '))
r = int(input('ведите радиус круга: '))
circle = Circle(x, y, r)
print('площать круга: ', circle.area_crl())
print('периметр круга: ', circle.perim_crl())
print("координаты центра круга: "+'(' + str(circle.X)+';'+ str(circle.Y)+')')
x = int(input('ведите  координату Х  центра  для перемешения круга: '))
y = int(input('ведите  координату Y  центра для перемешения круга: '))
print('центр круга перемещён на координату: ', circle.moveTo(x, y))
