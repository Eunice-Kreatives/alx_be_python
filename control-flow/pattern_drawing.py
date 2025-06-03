# pattern_drawing.py

def draw_square_pattern():
    """
    Prompts the user for a positive integer (size) and then
    draws a square pattern of asterisks (*) of that size using nested loops.
    Handles invalid or non-positive input.
    """
    # Prompt User for Pattern Size
    try:
        size_str = input("Enter the size of the pattern: ")
        size = int(size_str) # Convert input to an integer

        # Input validation: Ensure the size is a positive integer
        if size <= 0:
            print("Please enter a positive integer for the pattern size.")
            return # Exit the function if input is not positive
    except ValueError:
        print("Invalid input. Please enter a whole number for the pattern size.")
        return # Exit the function if input is not a valid integer

    # Draw the Pattern
    print(f"\nDrawing a {size}x{size} square pattern:")

    # First, use a while loop to iterate through each row of the pattern.
    row_counter = 0 # Start row counter from 0
    while row_counter < size:
        # Inside the while loop, use a for loop to print asterisks (*) side by side
        # The inner loop will run 'size' times for each row
        for _ in range(size):
            # print("*", end="") ensures asterisks are printed on the same line
            print("*", end="")
        
        # After completing each row (the inner for loop finishes),
        # print a newline character to move to the next row
        print() 
        
        # Increment the row counter for the while loop
        row_counter += 1

# Run the pattern drawing function when the script is executed
if __name__ == "__main__":
    draw_square_pattern()