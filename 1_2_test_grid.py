import tkinter as tk
import csv
from datetime import datetime
from pprint import pformat

win = tk.Tk()
win.title('testing grid')
win.geometry('1000x600')

text = tk.Text(win)
text.pack()

d = {
                    'operation': 'withdraw',
                    'how much': 100,
                    'comment': 'trololo',
                    'date': datetime.now()
                }

d2 = [d['operation'], d['how much'], d['comment'], d['date']]
text.insert(1.0, pformat(d2, width=text['width']))


tk.mainloop()