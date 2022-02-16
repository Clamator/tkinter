class Point:
    WIDTH = 10
    HEIGHT = 100
    # slots allows some vars only for exemplar on class, class can contain any vars
    # while trying to add non-allowed var you get an TypeError
    __slots__ = ['__x','__y','z', WIDTH, HEIGHT]
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.z = z

    def __check_instance(a):
        if isinstance(a, (int, float)):
            return True
        return False

    def setCoords(self, x, y, z):
        if Point.__check_instance(x) and Point.__check_instance(y):
            self.__x = x
            self.__y = y
            self.z = z
        else:
            print('not numbers')
            #raise TypeError('entered data is not numeric')

    def getCoords(self):
        return self.__x, self.__y, self.z

    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'Частная переменная'
        else:
            return object.__getattribute__(self, item)

    # this method check if the variable is WIDTH, if it is not - the var is being corrected,
    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError('WIDTH is not correctable')
        elif key == 'HEIGHT':
            print(f'{key} was corrected to {value}')
        else:
            # cnahge the local variable
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('__getattr__, variable does not exist: '+ item)

    def __delattr__(self, item):
        print(f'__delattr__, {item} was deleted')

pt = Point(2, 3, 5)
pt.setCoords(5, 10, 5)
print(pt.getCoords())

#pt.WIDTH = 10
pt.HEIGHT = 11
pt.z = 15
print(pt.z)
del pt.z

pt.var = 7