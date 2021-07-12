class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount 
        return self

    def display_user_balance(self):
        print(f"{self.name} with Email {self.email } now has a balance of {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

User_michael = User(username="Michael", email_address='fakeEmail@gmail.com')
User_michael.make_deposit(100)
User_michael.display_user_balance()
User_michael.make_withdrawal(50)
User_michael.display_user_balance()


User_william = User(username="William", email_address='fakeEmail2@gmail.com')
User_william.display_user_balance()

User_michael.transfer_money(other_user=User_william, amount= 10)
User_michael.display_user_balance()
User_william.display_user_balance()

User(username="User1", email_address='Email1@gmail.com').make_deposit(100).display_user_balance().make_withdrawal(50).display_user_balance()
User(username="User2", email_address='Email2@gmail.com').make_deposit(100).display_user_balance().make_withdrawal(100).display_user_balance()