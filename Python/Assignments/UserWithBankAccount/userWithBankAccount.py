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
        getattr(self, account).deposit(amount)
        return self

    def make_withdrawal(self, account, amount):
        getattr(self, account).withdrawal(amount)
        return self

    def display_user_balance(self, account):
        print(f"{self.name} with Email {self.email } now has a balance of {getattr(self, account).account_balance} in account1")
        return self

    def __str__(self):
        return self.name
        
user1 = User(username='User1', email_address='email1@gmail.com', int_rate=.05, balance=100)
user1.display_user_balance(account= 'account1')
user1.make_deposit(account = 'account1', amount = 100).display_user_balance('account1')

# print(user1)

