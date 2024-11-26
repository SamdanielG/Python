class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:  # Corrected attribute name
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance")

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(300)
