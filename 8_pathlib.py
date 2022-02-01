import tkinter as tk
import tkinter.ttk as ttk
import csv
from pathlib import *

win = tk.Tk()
columns=('operation', 'how_much', 'comment', 'date')

treeview = ttk.Treeview(win, show="headings", columns=columns, selectmode="browse")
treeview.column('operation', width=150,anchor='center')
treeview.column('how_much', width=150,anchor='center')
treeview.column('comment', width=150,anchor='center')
treeview.column('date', width=150,anchor='center')

treeview.heading('operation', text='operation')
treeview.heading('how_much', text='how much')
treeview.heading('comment', text='comment')
treeview.heading('date', text='date')

treeview.pack(side='left', fill='both', expand=tk.YES)
operation = ['Computer1', 'Server', 'Notebook']
how_much = ['10.13.71.223','10.25.61.186','10.25.11.163']
comment = ['1','2','3',]
date = ['5','5','5']


for i in range(min(len(operation), len(how_much))):
    treeview.insert('', tk.END, values=(operation[i], how_much[i], comment[i], date[i]))

win.mainloop()