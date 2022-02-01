import tkinter as tk
import tkinter.ttk as ttk
import csv
from pathlib import *

win = tk.Tk()
win.geometry('800x400+600+300')
columns=('operation', 'how_much', 'comment', 'date')

treeview = ttk.Treeview(win, show="headings", columns=columns, selectmode="browse")
treeview.column('operation', width=100,anchor='center')
treeview.column('how_much', width=100,anchor='center')
treeview.column('comment', width=250,anchor='center')
treeview.column('date', width=150,anchor='center')

treeview.heading('operation', text='operation')
treeview.heading('how_much', text='how much')
treeview.heading('comment', text='comment')
treeview.heading('date', text='date')

treeview.pack(side='left', fill='both', expand=tk.YES)
#operation = ['Computer1', 'Server', 'Notebook']
#how_much = ['10.13.71.223','10.25.61.186','10.25.11.163']
#comment = ['1','2','3',]
#date = ['5','5','5']

cur_path = Path.cwd()
com_his = cur_path/'wallet_project'/'categories'/'common_history.csv'
with open(com_his, mode='r') as file:
    order = ('operation', 'how much', 'comment', 'date')
    reader = csv.DictReader(file, fieldnames=order)
    main_lst = []
    for row in reader:
        main_lst.append(row)

    #for el in reversed(main_lst):
    #    print(el['operation'], el['how much'],el['comment'],el['date'])

for el in(main_lst):
    treeview.insert('', tk.END, values=(el['operation'], el['how much'],el['comment'],el['date']))

win.mainloop()

# treeview.insert('', tk.END, values=(operation[i], how_much[i], comment[i], date[i]))
# dict_values(['refill', '1000.0', 'salary', '2022-01-20 12:43:35.324424'])