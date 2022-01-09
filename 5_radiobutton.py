import tkinter as tk


def select_level():
    lvl = level.get()
    string = f'you chose {lvl}'
    level_text.set(string)
    if lvl == 1:
        print('easy')
    elif lvl == 2:
        print('middle')
    elif lvl == 3:
        print('hard')

def do_it_all():
    di = do_it.get()
    f'you decide - {di}'


win = tk.Tk()
win.title('entry testing')
win.geometry('600x600+750+300')

level = tk.IntVar()
level_text = tk.StringVar()
do_it = tk.StringVar()
do_it.set('Do not do it')

tk.Label(win, text='Choose your destiny').pack()

tk.Radiobutton(win, text='Easy', variable=level, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Middle', variable=level, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Hard', variable=level, value=3, command=select_level).pack()

tk.Checkbutton(win, textvariable=do_it, variable=do_it, command=do_it_all,
               indicatoron=1,
               offvalue='Do not do it',
               onvalue='Do it').pack()
tk.Label(win, textvariable=level_text).pack()


win.mainloop()
