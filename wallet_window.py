import tkinter as tk
win = tk.Tk()
win.geometry('430x380+600+300')
win.title('My wallet')
win['bg'] = 'yellow'


def refill():
    tk.Label(win, text='refill is done.', bg='yellow').place(x=120, y=150, relx=0, width=200, height=20)
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        new_total_money = money_amount + total_money
        tk.Label(win, text=f'It is {total_money} in the wallet now', bg='yellow', font=(None, 20)).place(x=0, y=10, relx=0, width=430, height=20)
        number.delete(0, tk.END)
        number.insert(0, '0')

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))


def withdraw():
    tk.Label(win, text='withdraw is done.', bg='yellow').place(x=120, y=150, relx=0, width=200, height=20)
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(number.get())
        new_total_money = total_money - money_amount
        tk.Label(win, text=f'It is {total_money} in the wallet now', bg='yellow', font=(None, 20)).place(x=0, y=10, relx=0, width=430, height=20)
        number.delete(0, tk.END)
        number.insert(0, '0')

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))

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

with open('wallet.txt', 'r', encoding='utf-8') as total_money:
    total_money = float(total_money.read())
    tk.Label(win, text=f'It is {total_money} in the wallet now', bg='yellow', font=(None, 20)).place(x=0, y=10, relx=0, width=430, height=20)
    tk.Label(win, text=f'Enter a necessary number', bg='yellow').place(x=0, y=50, relx=0, width=200, height=20)
    number = tk.Entry(win, justify=tk.RIGHT)
    number.insert(0, '0')
    number.place(x=200, y=50, relx=0, width=200, height=20)
    tk.Button(win, text='Refill', command=refill, bg='orange').place(x=50, y=90, relx=0, width=100, height=20)
    tk.Button(win, text='Withdraw', command=withdraw, bg='orange').place(x=250, y=90, width=100, height=20)


win.bind('<Key>', press_key)

if __name__ == '__main__':
    tk.mainloop()

#