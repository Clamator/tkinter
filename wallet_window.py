import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.geometry('400x480+600+300')
# win.attributes('-fullscreen', True)
win.title('My wallet')
win.minsize(400, 480)
win['bg'] = '#3b5998'

def about():
    win2 = tk.Tk()
    win2.geometry('600x400+600+300')
    win2.title('About/ How to use')
    info = open('categories\\about.txt')
    tk.Label(win2, text=info.read()).pack()
    win2.mainloop()


menubar = tk.Menu(win)
win.config(menu=menubar)
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label='About/ How to use', command=about)
settings_menu.add_command(label='Exit', command=win.destroy)
menubar.add_cascade(label='Settings', menu=settings_menu)


def add_spent_money_to_category(category, spent_money):
    if category == 'food':
        with open('categories\\food.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.05, rely=0.57,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)
        with open('categories\\food.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
            # print(f'{category}')

    elif category == 'transport pass':
        with open('categories\\transport pass.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.36, rely=0.57,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)
        with open('categories\\transport pass.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'entertainment':
        with open('categories\entertainment.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.67, rely=0.57,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)
        with open('categories\entertainment.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'medicine':
        with open('categories\medicine.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.05, rely=0.72,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)
        with open('categories\medicine.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'other':
        with open('categories\other.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='#3b5998', fg='white').place(relx=0.36, rely=0.72,
                                                                                            relwidth=0.3,
                                                                                            relheight=0.05)
        with open('categories\other.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))


def refill():
    tk.Label(win, text='refill has been done.', bg='#3b5998', fg='white').place(relx=0.5, rely=0.3, anchor='center',
                                                                                relwidth=0.4, relheight=0.07)
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        new_total_money = money_amount + total_money
        tk.Label(win, text=f'It is {new_total_money} in the wallet now', bg='#3b5998', font=(None, 20),
                 fg='white').place(relx=0.5, rely=0.05, anchor='center',
                                   width=430,
                                   height=20)
        number.delete(0, tk.END)
        number.insert(0, '0')

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))


def withdraw():
    tk.Label(win, text='withdraw has been done.', bg='#3b5998', fg='white').place(relx=0.5, rely=0.3, anchor='center',
                                                                                  relwidth=0.4, relheight=0.07)
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        if money_amount <= total_money:
            new_total_money = total_money - money_amount
            tk.Label(win, text=f'It is {new_total_money} in the wallet now', bg='#3b5998', font=(None, 20),
                     fg='white').place(relx=0.5, rely=0.05, anchor='center',
                                       width=430,
                                       height=20)
            number.delete(0, tk.END)
            number.insert(0, '0')
            current_category = combo_categories.get()
            add_spent_money_to_category(current_category, money_amount)
            with open('wallet.txt', 'w', encoding='utf-8') as wallet:
                wallet.write(str(new_total_money))
        else:
            messagebox.showerror('Attention', "you don't have money enough")
            tk.Label(win, text='withdraw has not been done.', bg='#3b5998', fg='white').place(relx=0.5, rely=0.3,
                                                                                              anchor='center',
                                                                                              relwidth=0.4,
                                                                                              relheight=0.07)
            number.delete(0, tk.END)
            number.insert(0, '0')


def add_digit(digit):
    value = number.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    number.delete(0, tk.END)
    number.insert(0, value + str(digit))


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char == 'w':
        withdraw()
    elif event.char == 'r':
        refill()
    elif event.char == 'c':
        number.delete(0, tk.END)
        number.insert(0, '0')


with open('wallet.txt', 'r', encoding='utf-8') as total_money:
    total_money = float(total_money.read())
    tk.Label(win, text=f'It is {total_money} in the wallet now', bg='#3b5998', font=(None, 20), fg='white').place(
        relx=0.5, rely=0.05, anchor='center',
        width=430,
        height=20)

tk.Label(win, text=f'Enter a necessary number ->', bg='#3b5998', fg='white').place(relx=0.05, rely=0.10, relwidth=0.4,
                                                                                   relheight=0.05)
tk.Label(win, text='Choose withdraw category', bg='#3b5998', fg='white').place(relx=0.05, rely=0.34, relwidth=0.4,
                                                                               relheight=0.05)
number = tk.Entry(win, justify=tk.RIGHT)
number.insert(0, '0')
number.place(relx=0.60, rely=0.10, relwidth=0.3, relheight=0.05)
tk.Button(win, text='Refill', command=refill, bg='white').place(relx=0.60, rely=0.2, relwidth=0.3, relheight=0.05)
tk.Button(win, text='Withdraw', command=withdraw, bg='white').place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.05)

tk.Button(win, text='food', bg='white').place(relx=0.05, rely=0.5, relwidth=0.28, relheight=0.05)
tk.Button(win, text='transport pass', bg='white').place(relx=0.36, rely=0.5, relwidth=0.28, relheight=0.05)
tk.Button(win, text='entertainment', bg='white').place(relx=0.67, rely=0.5, relwidth=0.28, relheight=0.05)
tk.Button(win, text='medicine', bg='white').place(relx=0.05, rely=0.65, relwidth=0.28, relheight=0.05)
tk.Button(win, text='other', bg='white').place(relx=0.36, rely=0.65, relwidth=0.28, relheight=0.05)

categories = ['food', 'transport pass', 'entertainment', 'medicine', 'other']
combo_categories = ttk.Combobox(win, values=categories)
combo_categories.current(0)
combo_categories.place(relx=0.60, rely=0.34, relwidth=0.3, relheight=0.05)

# shows how much has been spent for a category
with open('categories\\food.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.05, rely=0.57,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\\transport pass.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.36, rely=0.57,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\entertainment.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.67, rely=0.57,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\medicine.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.05, rely=0.72,
                                                                                      relwidth=0.3, relheight=0.05)

with open('categories\other.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='#3b5998', fg='white').place(relx=0.36, rely=0.72,
                                                                                      relwidth=0.3, relheight=0.05)

win.bind('<Key>', press_key)

if __name__ == '__main__':
    tk.mainloop()

#
