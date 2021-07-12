class BankAccount:
    def __init__(self, int_rate, balance):# now our method has 2 parameters!
        self.account_balance = balance		# the account balance is set to $0, so no need for a third parameter
        self.int_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawal(self, amount):
        self.account_balance -= amount 
        return self

    def display_account_info(self):
        print(f"Account now has a balance of {self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance *= (1 + self.int_rate)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

BankAccount(int_rate=.05, balance=100).deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()

BankAccount(int_rate=.05, balance=100).deposit(100).deposit(100).withdrawal(50).withdrawal(50).withdrawal(50).withdrawal(50).yield_interest().display_account_info()