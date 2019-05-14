class BankAccount:

    interest_rate = 0.12
    accounts = []

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'{self.name}'

    def deposit(self, dep_amount):
        self.balance += dep_amount
        return self.balance

    def withdraw(self, wdl_amount):
        self.balance -= wdl_amount
        return self.balance

    @classmethod
    def create(cls, name):
        cls.accounts.append(name)
    
    @classmethod
    def total_funds(cls):
        total_balance = 0
        for account in cls.accounts:
            total_balance += account.balance
        return total_balance

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate
            print(f'{account.name} - {account.balance}')

acc1 = BankAccount('savings')
acc2 = BankAccount('chequings')
acc3 = BankAccount('safedeposit')

BankAccount.create(acc2)
BankAccount.create(acc3)

print(acc2.balance)
print(BankAccount.total_funds())

acc2.deposit(200)
acc3.deposit(1000)

print(acc2.balance)
print(acc3.balance)

print(BankAccount.total_funds())

BankAccount.interest_time()

print(acc2.balance)
print(acc3.balance)
print(BankAccount.total_funds())

acc2.withdraw(50)

print(acc2.balance)

print(BankAccount.total_funds())