# main.py

# This line imports the function from your arithmetic.py file
import arithmetic_operations
from arithmetic_operations import perform_operation


def run_calculator():
    """
    This function gets input from the user and uses the perform_operation function.
    """
    print("\n--- Simple Calculator Program ---")

    try:
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str)

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str)

        operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

        result = perform_operation(num1, num2, operation)

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This ensures run_calculator() only runs when main.py is executed directly
if __name__ == "__main__":
    run_calculator()

    print("\n--- Additional examples using imported function ---")
    print(f"10.5 + 2.5 = {perform_operation(10.5, 2.5, 'add')}")
    print(f"3 * 7 = {perform_operation(3, 7, 'multiply')}")
    print(f"9 / 0 = {perform_operation(9, 0, 'divide')}") # Example of error handling