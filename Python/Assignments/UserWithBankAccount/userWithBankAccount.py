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

    def yield_interest(self):
        self.account_balance *= (1 + self.int_rate)
        return self

class User:
    def __init__(self, username, email_address, int_rate, balance):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account1 = BankAccount(int_rate, balance)		# the account balance is set to $0, so no need for a third parameter
        self.account2 = BankAccount(int_rate, balance)		# the account balance is set to $0, so no need for a third parameter

    def make_deposit(self, account, amount):
        if account == 'account1':
            self.account1.deposit(amount)
        if account == 'account2':      
            self.account2.deposit(amount)
        return self

    def make_withdrawal(self, account, amount):
        if account == 'account1':
            self.account1.withdrawal(amount)
        if account == 'account2':      
            self.account2.withdrawal(amount)
        return self

    def display_user_balance(self, account):
        if account == 'account1':   
            print(f"{self.name} with Email {self.email } now has a balance of {self.account1.account_balance} in account1")
        elif account == 'account2':   
            print(f"{self.name} with Email {self.email } now has a balance of {self.account2.account_balance} in account2")
        else:
            print(f"{self.name} with Email {self.email } now has a balance of {self.account1.account_balance} in account1")
            print(f"{self.name} with Email {self.email } now has a balance of {self.account2.account_balance} in account2")
        return self

User1 = User(username='User1', email_address='email1@gmail.com', int_rate=.05, balance=100)
User1.display_user_balance(account= 'account1')
User1.make_deposit(account = 'account1', amount = 100).display_user_balance('')
User1.display_user_balance()