class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.display_balance()

        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.balance)


acc_1 = BankAccount()

acc_1.deposit(20000)
acc_1.display_balance()
acc_1.withdraw(2000)
acc_1.withdraw(2000)
acc_1.withdraw(20000)
