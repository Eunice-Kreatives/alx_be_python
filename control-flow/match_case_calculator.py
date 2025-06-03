# match_case_calculator.py

def run_calculator():
    """
    Prompts the user for two numbers and an operation,
    then performs the calculation using a match-case statement.
    """
    # Prompt for User Input: Numbers
    try:
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str) # Use float to allow decimal numbers

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str) # Use float to allow decimal numbers
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return # Exit the function if numbers are not valid

    # Ask for the type of operation
    operation = input("Choose the operation (+, -, *, /): ")

    result = None # Initialize result to None
    
    # Perform the Calculation Using Match Case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            # Handle division by zero case gracefully
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _: # Handles any other input for operation
            print("Invalid operation. Please choose +, -, *, or /.")

# Run the calculator function
if __name__ == "__main__":
    run_calculator()