from Bank_account import BankAccount
class User:
    def __init__(self, name, account_balance):
        print(f"CREATING USER {name}")
        self.name = name
        self.account.balance(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        print(f"DEPOSITING ${amount} TO {self.name}")
        self.account.deposit()

    def make_withdrawal(self, amount):
        print(f"WITHDRAWING ${amount} FROM {self.name}")
        self.account.widthdrawal

    def display_user_balance(self):
        self.account.display_account_info
        print(f"GETTING ACCOUNT BALANCE FOR {self.name}")
        print(self.account_balance)

    def transfer_money(self, amount, recipient):
        print(f"TRANSFERING ${amount} FROM {self.name} TO {recipient.name}")
        self.make_withdrawal(amount)
        recipient.make_deposit(amount)



# paulie = User("Paul Smith", 500)

# paulie.make_withdrawal(250)

# paulie.display_user_balance()

# joe=User("Joseph Campbell", 700)
# joe.make_deposit(100)
# joe.make_deposit(200)
# joe.make_withdrawal(500)
# joe.display_user_balance()

# bob = User("Bob Ross", 100)
# bob.make_withdrawal(20)
# bob.make_withdrawal(10)
# bob.make_withdrawal(30)
# bob.display_user_balance()

# bob.transfer_money(1, joe)

# bob.display_user_balance()
# joe.display_user_balance()