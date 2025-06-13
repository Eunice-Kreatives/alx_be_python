# main-0.py
import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands:")
        print("  deposit:<amount> - Deposit money into the account.")
        print("  withdraw:<amount> - Withdraw money from the account.")
        print("  display - Display the current balance.")
        sys.exit(1) # Exit with an error code

    try:
        parts = sys.argv[1].split(':')
        command = parts[0].lower() 
        amount_str = parts[1] if len(parts) > 1 else None
    
    except IndexError:
        print("Error: Invalid command format. Use <command>:<amount> or <command>.")
        sys.exit(1)

    account = BankAccount(initial_balance=10000) 

    if command == 'deposit':
        try:
            amount = float(amount_str)
            account.deposit(amount)
        except (ValueError, TypeError):
            print("Error: For 'deposit', please provide a valid numeric amount.")
            sys.exit(1)
    elif command == 'withdraw':
        try:
            amount = float(amount_str)
            account.withdraw(amount)
        except (ValueError, TypeError):
            print("Error: For 'withdraw', please provide a valid numeric amount.")
            sys.exit(1)
    elif command == 'display':
        if amount_str is not None:
             print("Warning: 'display' command does not take an amount. Ignoring extra input.")
        account.display_balance()
    else:
        print(f"Error: Unknown command '{command}'.")
        print("Available commands: deposit, withdraw, display.")
        sys.exit(1)

if __name__ == "__main__":
    main()


