import tkinter as tk


def select_all():
    for check in [is_student, turn_on, ]:
        check.select()  # тут мы ставим галочку, так сказать


def deselect_all():
    for check in [is_student, turn_on, ]:
        check.deselect()  # снимаем галочки


def reverse_all():
    for check in [is_student, turn_on, ]:
        check.toggle()  # реверсируем выбор


def show_status():
    print('is student - ', is_student_value.get())


def show_lights():
    print('are lights turn on? ', turn_on_value.get())


win = tk.Tk()
win.title('entry testing')
win.geometry('600x600+750+300')

is_student_value = tk.StringVar()
is_student_value.set('No')
turn_on_value = tk.IntVar(0)  # 1 - вкл, 0 - выкл

is_student = tk.Checkbutton(win, text='Are you student?',
                            indicatoron=1,
                            variable=is_student_value,
                            offvalue='No',
                            onvalue='Yes')
turn_on = tk.Checkbutton(win, text='Turn on the lights', indicatoron=0,
                         variable=turn_on_value,
                         offvalue=0,
                         onvalue=1
                         )

is_student.pack()
turn_on.pack()

tk.Button(win, text='select all', command=select_all).pack()
tk.Button(win, text='deselect all', command=deselect_all).pack()
tk.Button(win, text='reverse all', command=reverse_all).pack()
tk.Button(win, text='show status', command=show_status).pack()
tk.Button(win, text='turn on lights', command=show_lights).pack()

win.mainloop()
