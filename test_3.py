from tkinter import *
import csv

root = Tk()

text = Text(width=100, height=40, bg="white",wrap=WORD)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

with open('printer.csv', 'r', newline='') as file:
    order = ['operation', 'how much', 'comment', 'date']
    reader = csv.DictReader(file, fieldnames=order)
    for row in reader:
        y = f"-{row['how much']}, {row['comment']}, date: {row['date'][:-10]} \n"
        text.insert(1.0, y)

root.mainloop()
