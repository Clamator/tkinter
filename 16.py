from typing import Literal, Final


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoors(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
            return True
        return False

    @ staticmethod
    def norm2(x, y):
        return x * x + y * y


c = lambda a, b: a*a + b*b
print(c(1,2))

lst = [x for x in range(-10,  11)]
def get_filtered_lst(lst, filter=None):
    if filter is None:
        return lst

    res = []
    for el in lst:
        if filter(el):
            res.append(el)
    return res

lst2 = get_filtered_lst(lst, lambda x: x % 2 ==0)
print(lst2)

def printer():
    print('Hello, World!')

c = lambda : printer()
c()

def open_file(file, mode: Literal['r', 'w', 'a']):
    pass

open_file('degrtge', 'w')
pi: Final = 3.14
pi = 1.2

