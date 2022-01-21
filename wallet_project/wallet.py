file = open('lection.txt')
file.read()

for row in file:
    print(row)

data_earned = open('categories\\total_spent.txt').read()
data_earned.write(money_amount)
data_earned.close

        data_earned = open('categories\\total_earned.txt', 'r')
        data_earned.read()
        data_earned.write(str(money_amount) + str(data_earned))
        data_earned = open('categories\\total_earned.txt', 'w')
        tk.Label(win, text=f'Total earned: \n{data}', bg='#3b5998', fg='green', font=(None, 15)).place(relx=0.55, rely=0.1,
                                                                                                       relwidth=0.4,
                                                                                                       relheight=0.1)