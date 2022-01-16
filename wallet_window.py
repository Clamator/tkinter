import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.geometry('430x480+600+300')
#win.attributes('-fullscreen', True)
win.title('My wallet')
win['bg'] = 'yellow'
categories = ['food', 'transport pass', 'entertainment', 'medicine', 'other']

menubar = tk.Menu(win)
win.config(menu=menubar)
settings_menu = tk.Menu(menubar)
settings_menu.add_command(label='About/ How to use')
settings_menu.add_command(label='Exit', command=win.destroy)
menubar.add_cascade(label='Settings', menu=settings_menu)


combo_categories = ttk.Combobox(win, values=categories)
combo_categories.current(0)
combo_categories.place(x=250, y=150, relx=0, width=120, height=20)

def add_spent_money_to_category(category, spent_money):
    if category == 'food':
        with open('categories\\food.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='yellow').place(x=0, y=210, relx=0, width=100, height=20)
        with open('categories\\food.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'transport pass':
        with open('categories\\transport.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='yellow').place(x=160, y=210, relx=0, width=100, height=20)
        with open('categories\\transport.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'entertainment':
        with open('categories\entertainment.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='yellow').place(x=300, y=210, relx=0, width=100, height=20)
        with open('categories\entertainment.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'medicine':
        with open('categories\medicine.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='yellow').place(x=0, y=270, relx=0, width=100, height=20)
        with open('categories\medicine.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))
    elif category == 'other':
        with open('categories\other.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'total spent: {new_money}', bg='yellow').place(x=160, y=270, relx=0, width=100, height=20)
        with open('categories\other.txt', 'w', encoding='utf-8') as cat:
            cat.write(str(new_money))

def refill():
    tk.Label(win, text='refill has been done.', bg='yellow').place(x=120, y=120, relx=0, width=200, height=20)
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        new_total_money = money_amount + total_money
        tk.Label(win, text=f'It is {new_total_money} in the wallet now', bg='yellow', font=(None, 20)).place(x=0, y=10, relx=0, width=430, height=20)
        number.delete(0, tk.END)
        number.insert(0, '0')

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))

def withdraw():
    tk.Label(win, text='withdraw has been done.', bg='yellow').place(x=120, y=120, relx=0, width=200, height=20)
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        if money_amount < total_money:
            new_total_money = total_money - money_amount
            tk.Label(win, text=f'It is {new_total_money} in the wallet now', bg='yellow', font=(None, 20)).place(x=0, y=10, relx=0, width=430, height=20)
            number.delete(0, tk.END)
            number.insert(0, '0')
            current_category = combo_categories.get()
            add_spent_money_to_category(current_category, money_amount)
            with open('wallet.txt', 'w', encoding='utf-8') as wallet:
                wallet.write(str(new_total_money))
        else:
            messagebox.showerror('Attention', "you don't have money enough")
            tk.Label(win, text='withdraw has not been done.', bg='yellow').place(x=120, y=120, relx=0, width=200, height=20)
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
    tk.Label(win, text=f'It is {total_money} in the wallet now', bg='yellow', font=(None, 20)).place(x=0, y=10, relx=0, width=430, height=20)
    tk.Label(win, text=f'Enter a necessary number ->', bg='yellow').place(x=0, y=50, relx=0, width=200, height=20)
    tk.Label(win, text='Choose withdraw category', bg='yellow').place(x=0, y=150, relx=0, width=200, height=20)
    number = tk.Entry(win, justify=tk.RIGHT)
    number.insert(0, '0')
    number.place(x=250, y=50, relx=0, width=100, height=20)
    tk.Button(win, text='Refill', command=refill, bg='orange').place(x=50, y=90, relx=0, width=100, height=20)
    tk.Button(win, text='Withdraw', command=withdraw, bg='orange').place(x=250, y=90, width=100, height=20)

    tk.Label(win, text='food', bg='yellow').place(x=0, y=190, relx=0, width=100, height=20)
    tk.Label(win, text='transport pass', bg='yellow').place(x=160, y=190, relx=0, width=100, height=20)
    tk.Label(win, text='entertainment', bg='yellow').place(x=300, y=190, relx=0, width=100, height=20)
    tk.Label(win, text='medicine', bg='yellow').place(x=0, y=250, relx=0, width=100, height=20)
    tk.Label(win, text='other', bg='yellow').place(x=160, y=250, relx=0, width=100, height=20)

with open('categories\\food.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='yellow').place(x=0, y=210, relx=0, width=100, height=20)

with open('categories\\transport.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='yellow').place(x=160, y=210, relx=0, width=100, height=20)

with open('categories\entertainment.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='yellow').place(x=300, y=210, relx=0, width=100, height=20)

with open('categories\medicine.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='yellow').place(x=0, y=270, relx=0, width=100, height=20)

with open('categories\other.txt', 'r', encoding='utf-8') as money:
    total_money = float(money.read())
    tk.Label(win, text=f'total spent: {total_money}', bg='yellow').place(x=160, y=270, relx=0, width=100, height=20)

win.bind('<Key>', press_key)

if __name__ == '__main__':
    tk.mainloop()

#