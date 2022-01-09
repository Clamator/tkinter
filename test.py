import time
import queue
import tkinter as tk
from tkinter import  ttk

def print_text(queue=None):
    tk.Label(win, text='Поиск начат').place(x=250, y=320, width=120, height=20)
    queue = queue.Queue()
    pb = ttk.Progressbar(length=300, orient=tk.HORIZONTAL).place(x=250, y=300, width=120, height=20)
    step = queue.get(0)
    pb.step(step * 100)
win = tk.Tk()
win.title('test')
win.geometry('600x400+300+200')

tk.Label(win, text='Ключевые слова:').place(x=10, y=10, width=120, height=20)
tk.Entry(win).place(x=130, y=10, width=120, height=20)

tk.Label(win, text='Заработная плата:').place(x=10, y=40, width=120, height=20)
tk.Entry(win).place(x=130, y=40, width=120, height=20)

tk.Button(win, text='Поиск!', command=print_text).place(x=250, y=350, width=120, height=20)





win.mainloop()