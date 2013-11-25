class BankAccount:
    def __init__(self, initial_balance):
        self.account = initial_balance 
        self.totalfee = 0
    def deposit(self, amount):
        self.account += amount
        """Deposits the amount into the account."""
    def withdraw(self, amount):
        if self.account-amount < 0:
            self.account -= amount+5
            self.totalfee += 5
        else:
            self.account -= amount
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
    def get_balance(self):
        return self.account
        """Returns the current balance in the account."""
    def get_fees(self):
        return self.totalfee
        """Returns the total fees ever deducted from the account."""
my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()