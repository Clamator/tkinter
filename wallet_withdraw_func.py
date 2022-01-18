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


def add_spent_money_to_category(category, spent_money):
    with open(f'categories\\{category}.txt', 'r', encoding='utf-8') as money:
        total_money = float(money.read())
        if total_money == '':
            total_money = 0
        new_money = total_money + float(spent_money)

    with open(f'categories\\{category}.txt', 'w', encoding='utf-8') as cat:
        cat.write(str(new_money))