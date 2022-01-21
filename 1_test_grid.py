#import tkinter as tk
#import csv
#from datetime import datetime
#import pathlib
#from pathlib import Path
#
#win = tk.Tk()
#win.title('testing grid')
#win.geometry('600x600')
#
#
#for i in range(3):
#    for j in range(4):
#        tk.Label(win, text=f'button {i}x{j}').grid(row=i, column=j, stick='we')
#
#win.grid_columnconfigure(0, minsize='100')
#win.grid_columnconfigure(1, minsize='150')
#
#tk.mainloop()

#earned_money = float(open('categories\\total_earned.txt').read())
        #new_earned_money = money_amount + earned_money
        #tk.Label(win, text=f'Total earned: \n{new_earned_money}', bg='#3b5998', fg='green', font=(None, 15)).place(relx=0.55,
        #                                                                                               rely=0.1,
        #                                                                                               relwidth=0.4,
        #                                                                                               relheight=0.1)
        #open('categories\\total_earned.txt', 'w').write(str(new_earned_money))


#new_spent_money2 = '0.0'
#tk.Label(win, text=f'Total spent: \n{new_spent_money2}', bg='#3b5998', fg='red',
#         font=(None, 15)).place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.1)
#open('categories\\total_spent.txt', 'w').write(str(new_spent_money2))
#
#new_earned_money2= '0.0'
#tk.Label(win, text=f'Total earned: \n{new_earned_money2}', bg='#3b5998', fg='#0fff83', font=(None, 15)).place(
#    relx=0.55,rely=0.1,relwidth=0.4,relheight=0.1)
#open('categories\\total_earned.txt', 'w').write(str(new_earned_money2))

lst = ['-' for x in range(80)]
x = ''.join(lst)


categories = ['common', 'food', 'transport', 'entertainment', 'medicine', 'other']
lst = ['-' for x in range(80)]
border = ''.join(lst)
for category in categories:
    open(f'categories\\{category}_history.csv', 'a', encoding="utf-8", newline='')
    writer = csv.writer(file)
    writer.writerow((data['operation']))
















