
class BankAccount:
    def __init__(self, balance, int_rate, account_name):
        self.balance = balance
        self.account_name = account_name
        self.int_rate= int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def widthdrawal(self, amount):
        self.balance -=amount
        return self 
    def display_account_info(self):
        print("Account Balance:$" , self.balance)
        print("Interest Rate:%" , self.int_rate)
        print("Account Name:" , self.account_name)
        return self
    def yield_interest(self):
        if (self.balance<0):
            print("Error: Balance insufficient")
            return self
        else:
            self.balance = self.balance +(self.balance * self.int_rate)
            return self

bobsBA = BankAccount(100,0.02,"checking")
chadsBA = BankAccount(200,0.03,"debit")
bobsBA.deposit(20).deposit(30).deposit(10).widthdrawal(50).display_account_info().yield_interest()
chadsBA.deposit(10).deposit(30).widthdrawal(5).widthdrawal(5).widthdrawal(5).widthdrawal(5).display_account_info().yield_interest()



