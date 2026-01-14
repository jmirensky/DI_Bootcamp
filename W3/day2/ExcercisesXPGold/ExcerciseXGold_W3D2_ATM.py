#Exercise 1: Bank Account
#Part IV

from ExcerciseXGold_W3D2_bankacc import BankAccount
from ExcerciseXGold_W3D2_bankacc import MinimumBalanceAccount

class ATM:
    """  Represents an ATM machine."""

    def __init__(self, account_list, try_limit):
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("Invalid account list")

        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try limit. Setting try_limit to 2.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n1. Log in")
            print("2. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye")
                break
            else:
                print("Invalid option")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                print("Login successful")
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print("Login failed")

        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. ATM shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                    print("New balance:", account.balance)

                elif choice == "2":
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                    print("New balance:", account.balance)

                elif choice == "3":
                    print("Logging out")
                    break
                else:
                    print("Invalid option")
            except Exception as e:
                print(e)