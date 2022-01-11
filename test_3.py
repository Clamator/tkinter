class Wallet():
    def refill(self):
        print('refill is in progress.')
        with open('wallet.txt', 'r', encoding='utf-8') as total_money:
            total_money = float(total_money.read())
            money_amount = float(input(f'What is the money amount?, it is {total_money} now'))
            new_total_money = money_amount + total_money
            print(f'it was {total_money}, now it is {new_total_money}')

        with open('wallet.txt', 'w', encoding='utf-8') as wallet:
            wallet.write(str(new_total_money))

    def withdraw(self):
        print('withdraw is in progress.')

        with open('wallet.txt', 'r', encoding='utf-8') as total_money:
            total_money = float(total_money.read())
            money_amount = float(input(f'What is the money amount?, it is {total_money} now'))
            new_total_money = total_money - money_amount
            print(f'it was {total_money}, now it is {new_total_money}')

        with open('wallet.txt', 'w', encoding='utf-8') as wallet:
            wallet.write(str(new_total_money))


if __name__ == '__main__':
    wallet = Wallet()
    while True:
        try:
            response = int(input('what to do? refill or withdraw? 1/2: '))
            if response == 1:
                wallet.refill()
            elif response == 2:
                wallet.withdraw()
            else:
                print('operation is over')
                break
        except ValueError:
            print('operation is over')
            break
