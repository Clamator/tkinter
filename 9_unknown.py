import tkinter as tk
import tkinter.ttk as ttk
import csv
from pathlib import *

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


root = tk.Tk()
cur_path = Path.cwd()
com_his = cur_path/'wallet_project'/'categories'/'common_history.csv'
with open(com_his, mode='r') as file:
    order = ('operation', 'how much', 'comment', 'date')
    reader = csv.DictReader(file, fieldnames=order)
    main_lst = []
    for row in reader:
        main_lst.append(row.values())
        #print(row)
    print(main_lst)
table = Table(root, headings=order, rows=(tuple(main_lst)))
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()