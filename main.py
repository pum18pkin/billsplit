#account = {
 #   "owner" : "almaz",
   # "balance" : 1500

#}
#daf deposit = (acc, amount):
    #acc["balance"] += amount
#account['balance'] = deposit 

# using oop 
#class name should alwayst start with capital letter
class Account:
    def __init__(self, owner, balance):# this are the attributes of the class 
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):# and this is the method of the class
        self.balance += amount

    def wisdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def statment(self): # self represents edom or the instance of the class
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self.balance} ETB")


edom =Account("edom", 1000) #this creates an account in the name of edom and with a balance of 1000
edom.deposit(400) # this will deposit 400 to the account of edom
edom.statment() # this will print the account owner and the balance of the account after deposit
edom.withdraw(900) # this will withdraw 900 from the account of edom


#almaz = Account("almaz", 1500) #this is an object / instance of the class Account
#almaz.deposit(1000) # ALSO THIS one too 

#print(almaz.balance) # this will print the balance of the account after deposit

#class person:
   # def __init__(self, name, address):
        #self.name = name 
        #self.address = address



