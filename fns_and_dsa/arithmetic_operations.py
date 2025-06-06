# arithmetic.py

def perform_operation(num1, num2, operation):
  """
  Performs an arithmetic operation on two numbers based on the specified operation.

  Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The type of operation ('add', 'subtract', 'multiply', 'divide').

  Returns:
    float or str: The result of the operation, or a specific message for division by zero.
  """

  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Error: Division by zero is not allowed."
    else:
      return num1 / num2
  else:
    return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

# This block is for testing arithmetic.py directly, and won't run when imported.
if __name__ == "__main__":
    print("--- Running internal tests for arithmetic.py ---")
    print(f"5.0 + 12.0 = {perform_operation(5.0, 12.0, 'add')}")
    # ... (other test cases omitted for brevity here, but they are in the full arithmetic.py)
    print("--- End of internal tests ---")


        


    
