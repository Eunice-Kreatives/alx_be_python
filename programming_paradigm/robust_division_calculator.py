# robust_division_calculator.py
def safe_divide(numerator, denominator):
    """
    Performs division, robustly handling division by zero and non-numeric inputs.

    Args:
        numerator_str (str): The string representation of the numerator.
        denominator_str (str): The string representation of the denominator.

    Returns:
        str: An error message if an error occurs, or the division result (float)
             formatted as a string.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero." 
        
    except ValueError:
        return "Error: Please enter numeric values only."

    except Exception as e:
        print(f"An unexpected error occured :{e}")

if __name__ =="__main__" :
    print("--- Testing safe_divide directly ---")
    print(safe_divide("10", "5"))        
    print(safe_divide("10", "0"))        
    print(safe_divide("ten", "5"))       
    print(safe_divide("10", "zero"))     
    print(safe_divide("abc", "xyz"))     
    print(safe_divide("20", "3")) 