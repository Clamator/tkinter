class Point:
    __count = 0
    __instance = None

    #method __new__ calls while creating a new examplar of class
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            Point.__count += 1
            cls.__instance = super(Point, cls).__new__(cls)
        else:
            print('class examplar is already exist')

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    @staticmethod
    def getCount():
        return Point.__count

pt1 = Point()
pt2 = Point()
pt3 = Point()
pt4 = Point()


print(Point.getCount())


class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sq = Rectangle.square(x, y)

    @staticmethod
    def square(x, y):
        sq = x * y
        return sq

    #def square2(self, x, y):
    #    self.sq = x * y
    #    return self.sq

sq1 = Rectangle(3, 5)
sq2 = Rectangle(5, 5)

print(sq1.sq, sq2.sq, sep= '\n')