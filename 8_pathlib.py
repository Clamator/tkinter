from pathlib import *
import csv

current_dir = Path.cwd()
home_dir = Path.home()

#print(current_dir, home_dir)

file1 = current_dir / 'printer.csv'
with open(file1,mode='r', newline='') as file:
    order = ['operation', 'how much', 'comment', 'date']
    reader = csv.DictReader(file, fieldnames=order)
    for row in reader:
        print(row)