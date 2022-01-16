import tkinter as tk

win = tk.Tk()
win.geometry('450x450+300+200')


def refill():
    print('refill is in progress.')
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(input(f'What is the money amount?, it is {total_money} now'))
        new_total_money = money_amount + total_money
        print(f'it was {total_money}, now it is {new_total_money}')

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))

def withdraw():
    print('withdraw is in progress.')
    with open('wallet.txt', 'r', encoding='utf-8') as total_money:
        total_money = float(total_money.read())
        money_amount = float(input(f'What is the money amount?, it is {total_money} now'))
        new_total_money = total_money - money_amount
        print(f'it was {total_money}, now it is {new_total_money}')

    with open('wallet.txt', 'w', encoding='utf-8') as wallet:
        wallet.write(str(new_total_money))

with open('wallet.txt', 'r', encoding='utf-8') as total_money:
    total_money = float(total_money.read())
    tk.Label(win, text=f'It is {total_money} now in the wallet').place(x=0, y=10, relx=0, width=200, height=20)
    tk.Label(win, text=f'Enter a necessary number').place(x=0, y=30, relx=0, width=200, height=20)
    tk.Entry(win).place(x=200, y=30, relx=0, width=200, height=20)
    tk.Button(win, text='Refill', command=refill).place(x=50, y=60, relx=0, width=100, height=20)
    tk.Button(win, text='Withdraw', command=withdraw).place(x=250, y=60, width=100, height=20)

if __name__ == '__main__':
    tk.mainloop()


