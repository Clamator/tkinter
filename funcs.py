def add_spent_money_to_category(category, spent_money):
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

    elif category == 'transport pass':
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

    else:
        messagebox.showerror('Attention', "unknown category")
        number.insert(0, '')