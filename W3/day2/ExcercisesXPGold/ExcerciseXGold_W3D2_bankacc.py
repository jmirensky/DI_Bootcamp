#Exercise 1: Bank Account
#Part I + II + III

class BankAccount:
    """Represents a basic bank account with authentication."""

    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False


    def authenticate(self, username, password):
        """ Authenticates the user. """
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False


    def deposit (self, amount):
        """  Deposits money into the account."""

        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Deposit amount must be positive")

        self.balance += amount


    def withdraw (self, amount):
        """ Withdraws money from the account."""
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Withdraw amount must be positive")

        if amount > self.balance:
            raise Exception("Insufficient funds")

        self.balance -= amount


class MinimumBalanceAccount(BankAccount):
    """ Bank account with a minimum balance restriction. """
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        """Withdraws money only if minimum balance is respected."""
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Withdraw amount must be positive")

        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: minimum balance reached")  #NO ENTIENDO ESTA LOGICA

        self.balance -= amount