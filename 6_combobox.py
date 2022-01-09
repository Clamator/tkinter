# комбобокс - это выбор одного из значений из окна
# он лежит немного в другом месте, его надо отдельно импортировать
# надо использовать метод current для того, чтобы комбобокс выбирал сразу какое-то значение по умолчанию
import tkinter as tk
from tkinter import ttk

week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

day = [x for x in range(1, 32)]
year = [x for x in range(1930, 2008)]


def show_date():
    print(combo.get(), combo_ints.get(), combo_year.get())

def set_date():
    combo.set('Friday')
    combo_ints.set(2)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'point {self.x}x{self.y}'


win = tk.Tk()
win.geometry('500x400+200+100')
win.title('testing combobox')
combo = ttk.Combobox(win, values=week)
combo_ints = ttk.Combobox(win, values=day)
combo_year = ttk.Combobox(win, values=year)
combo_point = ttk.Combobox(win, values=[Point(1, 1), Point(2, 4)])


combo.current(0)
combo_ints.current(0)
combo.place(x=10, y=10, width=120, height=20)
combo_ints.place(x=130, y=10, width=120, height=20)
combo_year.place(x=250, y=10, width=120, height=20)
combo_point.place(x=370, y=10, width=120, height=20)

ttk.Button(win, text='show date', command=show_date).place(x=200, y=80, width=100, height=30)
ttk.Button(win, text='set date', command=set_date).place(x=200, y=130, width=100, height=30)

win.mainloop()
