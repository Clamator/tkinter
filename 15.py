class Clock:
    __DAY = 86400
    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('seconds should be integer')

        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        return f'{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}'

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0'+str(x)

    def __getSecs(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ValueError('Operand should be of class type')

        return Clock(self.__secs + other.__getSecs())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ValueError('Operand should be of class type')

        self.__secs += other.__getSecs()
        return self

    def __eq__(self, other):
        return self.__getSecs() == other.__getSecs()

    def __nq__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            print('item should be a string')

        if item == 'hour':
            return (self.__secs // 3600) % 24
        elif item == 'min':
            return (self.__secs // 60) % 60
        elif item == 'sec':
            return self.__secs // 60
        else:
            raise ValueError('item is not in sec/min/hour')

clock = Clock(35100)
clock2 = Clock(200)
clock3 = Clock(300)
clock4 = Clock(300)
clock += clock2 + clock3
print(clock.getFormatTime())
print(clock['hour'])