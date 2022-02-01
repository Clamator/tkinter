import time
import tkinter as tk
import tkinter.ttk as ttk
import csv
from pathlib import *

win = tk.Tk()
win.title('wallet history')
win.geometry('800x400+600+300')
columns = ('operation', 'how_much', 'comment', 'date')
treeview = ttk.Treeview(win, show="headings", columns=columns, selectmode="browse")
treeview.column('operation', width=100, anchor='center')
treeview.column('how_much', width=100, anchor='center')
treeview.column('comment', width=250, anchor='center')
treeview.column('date', width=150, anchor='center')

treeview.heading('operation', text='operation')
treeview.heading('how_much', text='how much')
treeview.heading('comment', text='comment')
treeview.heading('date', text='date')

treeview.pack(side='left', fill='both', expand=tk.YES)

cur_path = Path.cwd()
com_his = cur_path / 'wallet_project' / 'categories' / 'common_history.csv'
with open(com_his, mode='r') as file:
    order = ('operation', 'how much', 'comment', 'date')
    reader = csv.DictReader(file, fieldnames=order)
    main_lst = []
    for row in reader:
        main_lst.append(row)

for el in main_lst:
    if 'refill' in el['operation']:
        treeview.insert('', tk.END, values=(el['operation'], f'+'+el['how much'], el['comment'], el['date'][:-10]))
    treeview.insert('', tk.END, values=(el['operation'], f'-' + el['how much'], el['comment'], el['date'][:-10]))

#time.sleep(5)
#treeview.delete(*treeview.get_children())
win.mainloop()
