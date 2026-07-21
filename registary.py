from abc import ABC, abstractmethod


class SMSAlert:
    def update(self, message):
        print("[SMS ALERT]", message)



class Account(ABC):
    def init(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.observers = []
        self.history = []  # Stack for transaction history

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self.history.append(f"Deposited {amount}")  # Push onto history stack
        self.notify(f"{self.owner} deposited {amount}. New balance = {self.balance}")

    @abstractmethod
    def statement(self):
        pass




class SavingsAccount(Account):
    def init(self, owner, account_number, balance=0, interest_rate=0.05):
        super().init(owner, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.notify(f"Interest added: {interest}. New balance = {self.balance}")

    def statement(self):
        print("----- Savings Account -----")
        print("Owner:", self.owner)
        print("Account No:", self.account_number)
        print("Balance:", self.balance)
        print("History:", self.history)
        print()




class CurrentAccount(Account):
    def init(self, owner, account_number, balance=0, overdraft_limit=0):
        super().init(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal denied: Overdraft limit exceeded.")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")  # Push onto history stack
            self.notify(f"{self.owner} withdrew {amount}. New balance = {self.balance}")

    def statement(self):
        print("----- Current Account -----")
        print("Owner:", self.owner)
        print("Account No:", self.account_number)
        print("Balance:", self.balance)
        print("Overdraft Limit:", self.overdraft_limit)
        print("History:", self.history)
        print()




class AccountRegistry:
    def init(self):
        self.accounts = {}

    # O(1)
    def add(self, account):
        self.accounts[account.account_number] = account

    # O(1)
    def find(self, account_number):
        return self.accounts.get(account_number)

    
    def list_all(self):
        return [self.accounts[key] for key in sorted(self.accounts)]




class AccountFactory:

    @staticmethod
    def create(account_type, owner, account_number, balance, extra):

        if account_type.lower() == "savings":
            return SavingsAccount(owner, account_number, balance, extra)

        elif account_type.lower() == "current":
            return CurrentAccount(owner, account_number, balance, extra)

        else:
            raise ValueError("Invalid account type")




sms = SMSAlert()

acc1 = AccountFactory.create(
    "savings",
    "Nahom",
    "001",
    3000,
    0.07
)

acc2 = AccountFactory.create(
    "current",
    "Dereje",
    "002",
    1600,
    800
)


acc1.subscribe(sms)
acc2.subscribe(sms)


registry = AccountRegistry()


registry.add(acc1)
registry.add(acc2)


acc1.deposit(500)
acc1.add_interest()

acc2.deposit(200)
acc2.withdraw(900)


found = registry.find("001")
if found:
    print("Found Account:", found.owner)
    print()

print("=== All Accounts ===")
for account in registry.list_all():
    account.statement()