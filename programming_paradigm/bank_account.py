# programming_paradigm.py

class BankAccount:
    """
    A class to represent the Bank account of a customer,
    demonstrating encapsulation of banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account.
                                     Defaults to 0 if not provided.
        """
        if initial_balance >= 0:
            self.__account_balance = float(initial_balance)
        else:
            self.__account_balance = 0.0
            print("Warning: Initial balance cannot be negative. Setting to 0.")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.__account_balance += amount 
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must always be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
        else:
            return False

    def display_balance(self):
        """
        Displays the current balance of the customer's account.
        """
        print(f"Current Balance: ${self.__account_balance:,.2f}")