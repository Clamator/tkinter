import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import csv
from datetime import datetime

win = tk.Tk()
win.geometry('400x480+600+300')
# win.attributes('-fullscreen', True)
win.title('My wallet')
win.minsize(400, 480)
win.maxsize(960, 1080)
win['bg'] = '#3b5998'


def about():
    win2 = tk.Tk()
    #win2.geometry('600x400+600+300')
    win2.title('About/ How to use')
    text = tk.Text(win2, width=100, height=40, bg="white", wrap=WORD)
    text.configure(state=tk.NORMAL)
    text.pack(side=LEFT)

    info = open('categories\\about.txt')
    text.insert(1.0, info.read())
    text.configure(state=tk.DISABLED)
    #tk.Label(win2, text=info.read()).pack()
    win2.mainloop()


menubar = tk.Menu(win)
win.config(menu=menubar)
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label='About/ How to use', command=about)
settings_menu.add_command(label='Exit', command=win.destroy)
menubar.add_cascade(label='Settings', menu=settings_menu)

categories = ['food', 'transport', 'entertainment', 'medicine', 'other']
combo_categories = ttk.Combobox(win, values=categories)
combo_categories.current(0)
combo_categories.place(relx=0.60, rely=0.2, relwidth=0.3, relheight=0.05)


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
    win3 = tk.Tk()
    win3.title('Wallet history')
    text = Text(win3, width=100, height=40, bg="white", wrap=WORD)
    text.pack(side=LEFT)
    scroll = Scrollbar(win3, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)
    with open('categories\\common_history.csv', 'r', encoding="utf-8") as file:
        order = ['operation', 'how much', 'comment', 'date']
        reader = csv.DictReader(file, fieldnames=order)
        text.configure(state=tk.NORMAL)
        for row in reader:
            x = f"op: {row['operation']}, +{row['how much']}$, {row['comment']}, date: {row['date'][:-10]} \n"
            y = f"op: {row['operation']}, -{row['how much']}$, {row['comment']}, date: {row['date'][:-10]} \n"
            if row['operation'] == 'refill':
                text.insert(1.0, x)
            else:
                text.insert(1.0, y)
        text.configure(state=tk.DISABLED)
def show_category_history(event):
    cat_name = event.widget.cget('text')
    win4 = tk.Tk()

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
            #tk.Label(win4, text=y, fg='green', bg='white').pack(anchor='w')
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


def refill():
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        new_total_money = money_amount + total_money
        tk.Button(win, text=f'It is {new_total_money} in the wallet now', bg='white', font=(None, 20), command=show_all_history).place(relx=0.5, rely=0.05, anchor='center',
                                                              width=380,
                                                              height=40)
        number.delete(0, tk.END)
        number.insert(0, '')

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
                tk.Button(win, text=f'It is {new_total_money} in the wallet now', bg='white', font=(None, 20), command=show_all_history).place(relx=0.5, rely=0.05, anchor='center',
                                                                      width=380,
                                                                      height=40)
                data = {
                    'operation': 'withdraw',
                    'how much': money_amount,
                    'comment': comment.get(),
                    'date': datetime.now()
                }

                write_csv(data)
                write_csv_categ(current_category, data)

            else:
                new_total_money = total_money
                messagebox.showerror('Attention', "Unknown category")
                combo_categories.current(0)
                tk.Button(win, text=f'It is {new_total_money} in the wallet now', bg='white', font=(None, 20), command=show_all_history).place(relx=0.5, rely=0.05, anchor='center',
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


tk.Label(win, text=f'Enter a necessary number ->', bg='#3b5998', fg='white').place(relx=0.05, rely=0.10, relwidth=0.4,
                                                                                   relheight=0.05)
tk.Label(win, text='Choose withdraw category ->', bg='#3b5998', fg='white').place(relx=0.05, rely=0.2, relwidth=0.4,
                                                                                  relheight=0.05)
number = tk.Entry(win, justify=tk.RIGHT)
# number.insert(0, '0')
number.place(relx=0.60, rely=0.10, relwidth=0.3, relheight=0.05)

comment = tk.Entry(justify=tk.RIGHT)
comment.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.7, height=20)

tk.Button(win, text='Refill', command=refill, bg='white').place(relx=0.60, rely=0.45, relwidth=0.3, relheight=0.05)
tk.Button(win, text='Withdraw', command=withdraw, bg='white').place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)

food = tk.Button(win, text='food', bg='white')
transport= tk.Button(win, text='transport', bg='white')
entertainment= tk.Button(win, text='entertainment', bg='white')
medicine= tk.Button(win, text='medicine', bg='white')
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

# shows how much there is money in the wallet
with open('wallet.txt', 'r', encoding='utf-8') as total_money:
    total_money = float(total_money.read())
    tk.Button(win, text=f'It is {total_money} in the wallet now', bg='white', font=(None, 20),
              command=show_all_history).place(
        relx=0.5, rely=0.05, anchor='center',
        width=380,
        height=40)
# shows how much has been spent for each category
with open('categories\\food.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.62,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\\transport.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.62,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\entertainment.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.66, rely=0.62,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\medicine.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.04, rely=0.77,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\other.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.35, rely=0.77,
                                                                                      relwidth=0.3, relheight=0.05)

if __name__ == '__main__':
    tk.mainloop()

#
