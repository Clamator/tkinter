import tkinter as tk
from funcs import print_text_in_console


def get_entry():
    value1 = name1.get()
    value2 = password.get()
    if value1 or value2:
        print(value1, value2)
        delete_entry()
    else:
        print('empty line')
        delete_entry()

def delete_entry():
    password.delete(0, 'end')
    name1.delete(0, tk.END)


win = tk.Tk()
win.title('entry testing')
win.geometry('600x600')

tk.Label(win, text='login').grid(row=0, column=0)
tk.Label(win, text='password').grid(row=1, column=0)

name1 = tk.Entry(win)
password = tk.Entry(win, show='●')

name1.grid(row=0, column=1)
password.grid(row=1, column=1)

# creating a button to get data
tk.Button(win, text='get', command=get_entry).grid(row=0, column=2, rowspan=2, stick='ns')
tk.Button(win, text='delete', command=delete_entry).grid(row=0, column=3, rowspan=2, stick='ns')
tk.Button(win, text='insert', command=lambda: name1.insert(0, 'hello')).grid(row=0, column=4)
tk.Button(win, text='insert', command=lambda: password.insert(0, 'world')).grid(row=1, column=4)

tk.mainloop()
