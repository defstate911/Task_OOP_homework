class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
        print(f'Вы успешно пополнили счет. Ваш баланс - {self.balance} рублей')

    def withdrawal(self, money): # снятие
        if money > self.balance:
            print(f'У вас недостаточно средств на счете')
        elif money <= self.balance:
            self.balance -= money
            print(f'Вы успешно сняли - {money} руб. Ваш остаток -{self.balance} рублей')

    def all_balance(self):
        print(f'Ваш баланс - {self.balance} рублей')

man = Account(12345, 600)
man.all_balance()
man.withdrawal(1000)
man.deposit(1500)
man.withdrawal(500)
man.withdrawal(1000)
man.deposit(100)
man.withdrawal(500)
man.all_balance()
