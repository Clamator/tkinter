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


other = float(open('categories\other.txt', 'r', encoding='utf-8').read())
tk.Label(win, text=f'total spent: {other}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.77,
                                                                                      relwidth=0.3, relheight=0.05)