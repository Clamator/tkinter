from typing import final


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def isDigit(self):
        if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
            return True
        return False

    def isInt(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            return True
        return False

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'green', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width

    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print('Coords should be numeric')


class Line(Prop):
    def __init__(self, *args):
        super().__init__(*args)
        self._color = 'red'

    def draw(self):
        print(f'drawing the {Line.__name__}: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')

    def setCoords(self, sp, ep):
        if sp.isInt() and ep.isInt():
            self._sp = sp
            self._ep = ep
        else:
            print('Coords should be integer')

class Rectan(Prop):
    def __init__(self, *args):
        super().__init__(*args)
        self.__width = 5

    def draw(self):
        print(f'drawing the {Rectan.__name__}: {self._sp}, {self._ep}, {self._color}, {self.__width}')


line = Line(Point(1, 2), Point(4, 6))
line.draw()
line.setCoords(Point(10, 20), Point(40, 60))
line.draw()

#rect = Rectan(Point(20, 30), Point(100, 120))
#rect.draw()


class Pers_PC:
    def __init__(self, ram=16, ssd=512, model='lenovo', cpu='11900'):
        self.ram = ram
        self.ssd = ssd
        self.model = model
        self.cpu = cpu

    def __str__(self):
        return f'model: {self.model}, ssd: {self.ssd}, cpu: {self.cpu}, ram: {self.ram}'


class Stac(Pers_PC):
    def __init__(self):
        super().__init__()
        self.monic = 'HP'
        self.keyboard = 'logitech'
        self.mouse = 'sven'

    def show_info(self):
        return f'{Pers_PC.__str__(self)}, keyboard {self.keyboard}, monic: {self.monic}, mouse: {self.mouse}'


class Laptop(Pers_PC):
    def __init__(self):
        super().__init__()
        self.size = '40x23x1.5'
        self.diagonal = 14.5

    def show_info(self):
        return f'{Pers_PC.__str__(self)}, size {self.size}, diagonal: {self.diagonal}'


#st = Stac()
#print(st.show_info())
#lt = Laptop()
#print(lt.show_info())

#@final
class Table:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b


class RectTable(Table):
    def __init__(self, *args):
        print('creating rectangle table')
        super().__init__(*args)

    def countS(self):
        print('counting s')
        return self.a * self.b


class CircleTable(Table):
    def __init__(self, *args):
        print('creating circle table')
        super().__init__(*args)

    def countS(self):
        print('counting s')
        if self.b is None:
            return 3.14 * (self.a**2)


table = Table()
rt1 = RectTable(2, 3)
print(rt1.countS())
ct1 = CircleTable(3)
print(ct1.countS())