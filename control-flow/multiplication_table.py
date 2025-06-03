# multiplication_table.py

def generate_multiplication_table():
    """
    Prompts the user for a number and prints its multiplication table from 1 to 10.
    Handles invalid input for the number gracefully.
    """
    # Prompt User for a Number
    try:
        number_str = input("Enter a number to see its multiplication table: ")
        number = int(number_str) # Convert the input string to an integer
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return # Exit the function if input is not a valid integer

    print(f"\nMultiplication Table for {number}:")

    # Generate and Print the Multiplication Table
    # Use a for loop to iterate through the numbers 1 to 10.
    # range(1, 11) generates numbers from 1 up to (but not including) 11,
    # which means 1, 2, 3, ..., 10.
    for i in range(1, 11):
        # For each iteration, calculate the product
        product = number * i
        
        # Print each line of the multiplication table in the specified format
        print(f"{number} * {i} = {product}")

# Run the function to generate the table when the script is executed
if __name__ == "__main__":
    generate_multiplication_table()