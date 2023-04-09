class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
            self.balance-=5
            return self
        else:
            self.balance -= amount
            return self
        
    def display_account_info(self):
        print("Balance: $"+ str(self.balance))
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(self.int_rate+1)
        return self


user1=BankAccount(0.01,825)
user2=BankAccount(0.01,790)

user1.deposit(80).deposit(130).deposit(280).withdraw(98).yield_interest().display_account_info()
user2.deposit(85).deposit(190).withdraw(45).withdraw(60).withdraw(50).withdraw(125).yield_interest().display_account_info()