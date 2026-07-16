#account = {
 #   "owner" : "almaz",
   # "balance" : 1500

#}
#daf deposit = (acc, amount):
    #acc["balance"] += amount
#account['balance'] = deposit 

# using oop 
#class name should alwayst start with capital letter
#class Account:
    #def __init__(self, owner, balance):# this are the attributes of the class 
       # self.owner = owner
       # self.balance = balance

    #def deposit(self, amount):# and this is the method of the class
      #  self.balance += amount

    #def wisdraw(self, amount):
       # if amount > self.balance:
         #   print("Insufficient funds")
       # else:
           # self.balance -= amount
    #def statment(self): # self represents edom or the instance of the class
        #print(f"Account owner: {self.owner}")
       # print(f"Account balance: {self.balance} ETB")


#edom =Account("edom", 1000) #this creates an account in the name of edom and with a balance of 1000
#edom.deposit(400) # this will deposit 400 to the account of edom
#edom.statment() # this will print the account owner and the balance of the account after deposit
#edom.withdraw(900) # this will withdraw 900 from the account of edom


#almaz = Account("almaz", 1500) #this is an object / instance of the class Account
#almaz.deposit(1000) # ALSO THIS one too 

#print(almaz.balance) # this will print the balance of the account after deposit

#class person:
   # def __init__(self, name, address):
        #self.name = name 
        #self.address = address
from abc import ABC, abstractmethod
class account(ABC) :
    def __init__(self, owner, account_number, balance=0, interest_rate=0.01, type="none"):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
        self.type = type
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance
    @abstractmethod
    def statment(self):
        if self.type == "savings":
            return self.balance + self.balance * self.interest_rate
        else 
            return self.balance
class SavinAcc(account):
    def __init__(self, owner, account_number, balance=0, interest_rate=0.01):
        super().__init__(owner, account_number, balance, interest_rate, type="savings")

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckINAcc(account):
    def __init__(self, owner, account_number, balance=0, overdraft_limit=0):
        super().__init__(owner, account_number, balance, interest_rate=0.01)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds: withdrawal exceeds balance and overdraft limit.")
        self.balance -= amount
    def statment(self):
        return self.balance

edom = SavinAcc("edom", "001", 1000)
print(edom.statment())  # This will print the balance after applying interest
print()
def total_interest(accounts):
    return sum(a.interest)
    total = 0
    for account in accounts:
        if isinstance(account, SavinAcc):
            total += account.balance * account.interest_rate
    return total