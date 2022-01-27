import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np

win = tk.Tk()
win.geometry('400x480+600+300')
# win.attributes('-fullscreen', True)
win.title('My wallet')
win.minsize(400, 480)
# win.maxsize(960, 960)
win['bg'] = '#3b5998'


def about():
    win2 = tk.Toplevel()
    win2.resizable(False, False)
    # win2.geometry('600x400+600+300')
    win2.title('About/ How to use')
    text = tk.Text(win2, width=100, height=40, bg="white", wrap=WORD)
    text.configure(state=tk.NORMAL)
    text.pack(side=LEFT)

    info = open('categories\\about.txt')
    text.insert(1.0, info.read())
    text.configure(state=tk.DISABLED)
    # tk.Label(win2, text=info.read()).pack()
    win2.mainloop()


def show_pie_chart():
    win_pie = tk.Toplevel()
    win_pie.title('Pie chart')
    win_pie.geometry('500x500+600+200')
    #win_pie.resizable(False, False)
    fig = plt.Figure(figsize=(12, 8), dpi=100)
    ax = fig.add_subplot(111)
    cat_vals = []
    result_labels = []
    labels = ['food', 'transport', 'entertainment', 'medicine', 'other']
    for label in labels:
        with open(f'categories\\{label}.txt', 'r', encoding='utf-8') as file:
            data = float(file.read())
            if data != 0.0:
                cat_vals.append(data)
                result_labels.append(label)
    #exp = (0.05, 0.05, 0.05, 0.05, 0.05)
    ax.pie(cat_vals, labels=result_labels, autopct='%.2f', shadow=True)
    circle = plt.Circle((0, 0), 0.5, color='white')
    ax.add_artist(circle)
    canvas = FigureCanvasTkAgg(fig, master=win_pie)
    canvas.get_tk_widget().pack()
    canvas.draw()
    plt.show()


menubar = tk.Menu(win)
win.config(menu=menubar)
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label='Show pie chart', command=show_pie_chart)
settings_menu.add_command(label='About/ How to use', command=about)
settings_menu.add_command(label='Exit', command=win.destroy)
menubar.add_cascade(label='Options', menu=settings_menu)


def write_csv(data):
    with open('categories\\common_history.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['operation'],
            data['how much'],
            data['comment'],
            data['date']
        ))


def write_csv_categ(current_category, data):
    cat_name = current_category
    with open(f'categories\\{cat_name}_history.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['operation'],
            data['how much'],
            data['comment'],
            data['date']
        ))


def show_all_history():
    win3 = tk.Toplevel()
    win3.title('Wallet history')
    win3.resizable(False, False)
    menubar2 = tk.Menu(win3)
    win3.config(menu=menubar2)

    text = tk.Text(win3, width=100, height=40, bg="white", wrap=WORD)
    text.pack(side=LEFT)
    scroll = Scrollbar(win3, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)
    with open('categories\\common_history.csv', 'r', encoding="utf-8") as file:
        order = ['operation', 'how much', 'comment', 'date']
        reader = csv.DictReader(file, fieldnames=order)
        text.configure(state=tk.NORMAL)
        for row in reader:
            x = f"op: {row['operation']}, +{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
            y = f"op: {row['operation']}, -{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
            if row['operation'] == 'refill':
                text.insert(1.0, x)
            else:
                text.insert(1.0, y)
        text.configure(state=tk.DISABLED)

    def show_refill():
        text.configure(state=tk.NORMAL)
        text.delete("1.0", "end")
        with open('categories\\common_history.csv', 'r', encoding="utf-8") as file:
            order = ['operation', 'how much', 'comment', 'date']
            reader = csv.DictReader(file, fieldnames=order)
            for row in reader:
                x = f"op: {row['operation']}, +{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
                if row['operation'] == 'refill':
                    text.insert(1.0, x)
            text.configure(state=tk.DISABLED)

    def show_withdraw():
        text.configure(state=tk.NORMAL)
        text.delete("1.0", "end")
        with open('categories\\common_history.csv', 'r', encoding="utf-8") as file:
            order = ['operation', 'how much', 'comment', 'date']
            reader = csv.DictReader(file, fieldnames=order)
            for row in reader:
                y = f"op: {row['operation']}, +{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
                if row['operation'] == 'withdraw':
                    text.insert(1.0, y)
            text.configure(state=tk.DISABLED)

    def show_all():
        with open('categories\\common_history.csv', 'r', encoding="utf-8") as file:
            order = ['operation', 'how much', 'comment', 'date']
            reader = csv.DictReader(file, fieldnames=order)
            text.configure(state=tk.NORMAL)
            for row in reader:
                x = f"op: {row['operation']}, +{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
                y = f"op: {row['operation']}, -{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
                if row['operation'] == 'refill':
                    text.insert(1.0, x)
                else:
                    text.insert(1.0, y)
            text.configure(state=tk.DISABLED)

    settings_menu2 = tk.Menu(menubar2, tearoff=0)
    settings_menu2.add_command(label='Show only refill', command=show_refill)
    settings_menu2.add_command(label='Show only withdraw', command=show_withdraw)
    settings_menu2.add_command(label='Show all', command=show_all)
    menubar2.add_cascade(label='Settings', menu=settings_menu2)


def show_category_history(event):
    cat_name = event.widget.cget('text')
    win4 = tk.Toplevel()
    win4.resizable(False, False)
    win4.title(f'{cat_name}')
    text = Text(win4, width=100, height=40, bg="white", wrap=WORD)
    text.pack(side=LEFT)

    scroll = Scrollbar(win4, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.configure(state=tk.NORMAL)
    text.config(yscrollcommand=scroll.set)
    with open(f'categories\\{cat_name}_history.csv', 'r', encoding="utf-8") as file:
        order = ['operation', 'how much', 'comment', 'date']
        reader = csv.DictReader(file, fieldnames=order)
        for row in reader:
            y = f"-{row['how much']} $, {row['comment']}, date: {row['date'][:-10]} \n"
            # tk.Label(win4, text=y, fg='green', bg='white').pack(anchor='w')
            text.insert(1.0, y)
        text.configure(state=tk.DISABLED)


def add_spent_money_to_category(category, spent_money):
    try:
        with open(f'categories\\{category}.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)

        with open(f'categories\\{category}.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))

        if category == 'food':
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.62,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)

        elif category == 'transport':
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.62,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)

        elif category == 'entertainment':
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.66, rely=0.62,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)

        elif category == 'medicine':
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.77,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)
        elif category == 'other':
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.77,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)

    except:
        messagebox.showerror('Attention', "unknown category")
        number.insert(0, '')


def delete_all_history():
    categories = ['food', 'transport', 'entertainment', 'medicine', 'other']
    null_amount_new = '0.0'
    for category in categories:
        amount = open(f'categories\\{category}.txt', 'w', encoding='utf-8')
        amount.write(str(null_amount_new))
        tk.Label(win, text=f'total spent: {null_amount_new}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.62,
                                                                                              relwidth=0.3,
                                                                                              relheight=0.05)

        tk.Label(win, text=f'total spent: {null_amount_new}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.62,
                                                                                              relwidth=0.3,
                                                                                              relheight=0.05)

        tk.Label(win, text=f'total spent: {null_amount_new}', bg='#3b5998', fg='white').place(relx=0.66, rely=0.62,
                                                                                              relwidth=0.3,
                                                                                              relheight=0.05)

        tk.Label(win, text=f'total spent: {null_amount_new}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.77,
                                                                                              relwidth=0.3,
                                                                                              relheight=0.05)

        tk.Label(win, text=f'total spent: {null_amount_new}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.77,
                                                                                              relwidth=0.3,
                                                                                              relheight=0.05)

    new_spent_money2 = '0.0'
    tk.Label(win, text=f'Total spent: \n{new_spent_money2}', bg='#3b5998', fg='red',
             font=(None, 15)).place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.1)
    open('categories\\total_spent.txt', 'w').write(str(new_spent_money2))

    new_earned_money2 = '0.0'
    tk.Label(win, text=f'Total earned: \n{new_earned_money2}', bg='#3b5998', fg='#0fff83', font=(None, 15)).place(
        relx=0.55, rely=0.1, relwidth=0.4, relheight=0.1)
    open('categories\\total_earned.txt', 'w').write(str(new_earned_money2))


def refill():
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        new_total_money = money_amount + total_money
        tk.Button(win, text=f'It is {new_total_money} in the wallet now', bg='white', font=(None, 20),
                  command=show_all_history).place(relx=0.5, rely=0.05, anchor='center',
                                                  width=380,
                                                  height=40)
        number.delete(0, tk.END)
        number.insert(0, '')

        earned_money = float(open('categories\\total_earned.txt').read())
        new_earned_money = money_amount + earned_money
        tk.Label(win, text=f'Total earned: \n{new_earned_money}', bg='#3b5998', fg='#0fff83', font=(None, 15)).place(
            relx=0.55,
            rely=0.1,
            relwidth=0.4,
            relheight=0.1)
        open('categories\\total_earned.txt', 'w').write(str(new_earned_money))

        messagebox.showinfo('Refilling', f"you refilled your willet with {money_amount}")
        data = {
            'operation': 'refill',
            'how much': money_amount,
            'comment': comment.get(),
            'date': datetime.now()
        }
        write_csv(data)

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))
    comment.delete(0, tk.END)


def withdraw():
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        if money_amount <= total_money:
            new_total_money = total_money - money_amount
            current_category = combo_categories.get()
            if current_category in categories:
                add_spent_money_to_category(current_category, money_amount)
                with open('wallet.txt', 'w', encoding='utf-8') as wallet:
                    wallet.write(str(new_total_money))
                messagebox.showinfo('Withdrawing', f"you have spent {money_amount} on {current_category}")
                tk.Button(win, text=f'It is {new_total_money} in the wallet now', bg='white', font=(None, 20),
                          command=show_all_history).place(relx=0.5, rely=0.05, anchor='center',
                                                          width=380,
                                                          height=40)
                data = {
                    'operation': 'withdraw',
                    'how much': money_amount,
                    'comment': comment.get(),
                    'date': datetime.now()
                }
                spent_money1 = float(open('categories\\total_spent.txt').read())
                new_spent_money1 = money_amount + spent_money1
                tk.Label(win, text=f'Total spent: \n{new_spent_money1}', bg='#3b5998', fg='red',
                         font=(None, 15)).place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.1)
                open('categories\\total_spent.txt', 'w').write(str(new_spent_money1))
                write_csv(data)
                write_csv_categ(current_category, data)

            else:
                new_total_money = total_money
                messagebox.showerror('Attention', "Unknown category")
                combo_categories.current(0)
                tk.Button(win, text=f'It is {new_total_money} in the wallet now', bg='white', font=(None, 20),
                          command=show_all_history).place(relx=0.5, rely=0.05, anchor='center',
                                                          width=380,
                                                          height=40)
        else:
            messagebox.showerror('Attention', "you don't have money enough")
            # tk.Label(win, text='withdraw has not been done.', bg='#3b5998', fg='white').place(relx=0.5, rely=0.3,
            #                                                                                  anchor='center',
            #                                                                                  relwidth=0.4,
            #                                                                                  relheight=0.07)
    number.delete(0, tk.END)
    comment.delete(0, tk.END)


def add_digit(digit):
    value = number.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    number.delete(0, tk.END)
    number.insert(0, value + str(digit))


# def press_key(event):
#    if event.char.isdigit():
#        add_digit(event.char)
#    elif event.char == 'w':
#        withdraw()
#    elif event.char == 'r':
#        refill()
#    elif event.char == 'c':
#        number.delete(0, tk.END)
#        number.insert(0, '0')
# win.bind('<Key>', press_key)

file = float(open('categories\\total_spent.txt').read())
tk.Label(win, text=f'Total spent: \n{file}', bg='#3b5998', fg='red', font=(None, 15)).place(relx=0.05, rely=0.1,
                                                                                            relwidth=0.4, relheight=0.1)

file2 = float(open('categories\\total_earned.txt').read())
tk.Label(win, text=f'Total earned: \n{file2}', bg='#3b5998', fg='#0fff83', font=(None, 15)).place(relx=0.55, rely=0.1,
                                                                                                  relwidth=0.4,
                                                                                                  relheight=0.1)

tk.Label(win, text=f'Enter a necessary number ->', bg='#3b5998', fg='white').place(relx=0.05, rely=0.2, relwidth=0.4,
                                                                                   relheight=0.05)
tk.Label(win, text='Choose withdraw category ->', bg='#3b5998', fg='white').place(relx=0.05, rely=0.3, relwidth=0.4,
                                                                                  relheight=0.05)
number = tk.Entry(win, justify=tk.RIGHT)
# number.insert(0, '0')
number.place(relx=0.60, rely=0.2, relwidth=0.3, relheight=0.05)

categories = ['food', 'transport', 'entertainment', 'medicine', 'other']
combo_categories = ttk.Combobox(win, values=categories)
combo_categories.current(0)
combo_categories.place(relx=0.60, rely=0.3, relwidth=0.3, relheight=0.05)

comment = tk.Entry(justify=tk.RIGHT)
comment.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.7, height=20)

tk.Button(win, text='Refill', command=refill, bg='white').place(relx=0.60, rely=0.45, relwidth=0.3, relheight=0.05)
tk.Button(win, text='Withdraw', command=withdraw, bg='white').place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)

food = tk.Button(win, text='food', bg='white')
transport = tk.Button(win, text='transport', bg='white')
entertainment = tk.Button(win, text='entertainment', bg='white')
medicine = tk.Button(win, text='medicine', bg='white')
other = tk.Button(win, text='other', bg='white')

food.place(relx=0.05, rely=0.55, relwidth=0.28, relheight=0.05)
transport.place(relx=0.36, rely=0.55, relwidth=0.28, relheight=0.05)
entertainment.place(relx=0.67, rely=0.55, relwidth=0.28, relheight=0.05)
medicine.place(relx=0.05, rely=0.7, relwidth=0.28, relheight=0.05)
other.place(relx=0.36, rely=0.7, relwidth=0.28, relheight=0.05)

food.bind('<Button-1>', show_category_history)
transport.bind('<Button-1>', show_category_history)
entertainment.bind('<Button-1>', show_category_history)
medicine.bind('<Button-1>', show_category_history)
other.bind('<Button-1>', show_category_history)

tk.Button(win, text='Delete all history', bg='white', command=delete_all_history).place(relx=0.67, rely=0.9,
                                                                                        relwidth=0.28, relheight=0.05)

# shows how much there is money in the wallet
wallet1 = float(open('wallet.txt', 'r', encoding='utf-8').read())
tk.Button(win, text=f'It is {wallet1} in the wallet now', bg='white', font=(None, 20),
          command=show_all_history).place(
    relx=0.5, rely=0.05, anchor='center',
    width=380,
    height=40)
# shows how much has been spent for each category
food1 = float(open('categories\\food.txt', 'r', encoding='utf-8').read())
tk.Label(win, text=f'total spent: {food1}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.62,
                                                                            relwidth=0.3, relheight=0.05)

transport1 = float(open('categories\\transport.txt', 'r', encoding='utf-8').read())
tk.Label(win, text=f'total spent: {transport1}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.62,
                                                                                 relwidth=0.3, relheight=0.05)

entertainment1 = float(open('categories\entertainment.txt', 'r', encoding='utf-8').read())
tk.Label(win, text=f'total spent: {entertainment1}', bg='#3b5998', fg='white').place(relx=0.66, rely=0.62,
                                                                                     relwidth=0.3, relheight=0.05)

medicine1 = float(open('categories\medicine.txt', 'r', encoding='utf-8').read())
tk.Label(win, text=f'total spent: {medicine1}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.77,
                                                                                relwidth=0.3, relheight=0.05)

other1 = float(open('categories\other.txt', 'r', encoding='utf-8').read())
tk.Label(win, text=f'total spent: {other1}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.77,
                                                                             relwidth=0.3, relheight=0.05)

if __name__ == '__main__':
    tk.mainloop()

#
