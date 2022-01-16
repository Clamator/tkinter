def add_spent_money_to_category(category, spent_money):
    if category == 'food':
        with open('categories\\food.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'{new_money}').place(x=0, y=210, relx=0, width=100, height=20)
        with open('categories\\food.txt', 'w', encoding='utf-8') as cat:
            cat.write(new_money)
    elif category == 'transport pass':
        with open('categories\\transport.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'{new_money}').place(x=160, y=210, relx=0, width=100, height=20)
        with open('categories\\transport.txt', 'w', encoding='utf-8') as cat:
            cat.write(new_money)
    elif category == 'entertainment':
        with open('categories\entertainment.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'{new_money}').place(x=300, y=210, relx=0, width=100, height=20)
        with open('categories\entertainment.txt', 'w', encoding='utf-8') as cat:
            cat.write(new_money)
    elif category == 'medicine':
        with open('categories\medicine.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'{new_money}').place(x=0, y=270, relx=0, width=100, height=20)
        with open('categories\medicine.txt', 'w', encoding='utf-8') as cat:
            cat.write(new_money)
    elif category == 'other':
        with open('categories\other.txt', 'r', encoding='utf-8') as money:
            total_money = float(money.read())
            if total_money == '':
                total_money = 0
            new_money = total_money + float(spent_money)
            tk.Label(win, text=f'{new_money}').place(x=160, y=270, relx=0, width=100, height=20)
        with open('categories\other.txt', 'w', encoding='utf-8') as cat:
            cat.write(new_money)