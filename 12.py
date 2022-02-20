# property
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_instance(a):
        if isinstance(a, (int, float)):
            return True
        return False

    # make methods private
    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        if Point.__check_instance(x):
            self.__x = x
        else:
            raise TypeError('not numeric input')

    @coordX.deleter
    def coordX(self):
        print('deleting coordX')
        del self.__x

    # coordX = property(__getCoordX, __setCoordX, __delCoordX)


class CoordValue:

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point2:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt2 = Point2(5, 10)
pt2.coordX = 15
pt2.coordY = 25
print(pt2.coordX, pt2.coordY)

pt3 = Point2(7, 17)
pt3.coordX = 11
pt3.coordY = 22
print(pt3.coordX, pt3.coordY)


class Calendar:
    __slots__ = ['__day', '__month', '__year']

    def __init__(self, day=1, month=1, year=2000):
        self.__day = day
        self.__month = month
        self.__year = year

    def __check_instance(a):
        if isinstance(a, (int, float)):
            return True
        return False

    def set_date(self, day, month, year):
        if Calendar.__check_instance(day) and Calendar.__check_instance(month) and Calendar.__check_instance(year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            print('not numbers')

    def get_date(self):
        return self.__day, self.__month, self.__year


cal = Calendar(2, 2, 2002)
cal.set_date(3, 3, 2003)
print(cal.get_date())


class DotsDescr:
    def __set_name__(self, owner, name):
        self.__name__ = name

    def __set__(self, instance, value):
        instance.__dict__[self.__name__] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name__]


class Rectangle:
    coordx = DotsDescr()
    coordy = DotsDescr()

    def __init__(self, x, y):
        self.coordx = x
        self.coordy = y


line1 = Rectangle(1, 2)
line2 = Rectangle(3, 4)

print(line1.coordx, line1.coordy)

