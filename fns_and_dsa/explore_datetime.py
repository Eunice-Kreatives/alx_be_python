from datetime import datetime, timedelta
def display_current_datetime():
    """
    Obtains and displays the current date and time in a readable format.
    """
  # Get the current date and time using datetime.now()
    current_datetime = datetime.now()
    #Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    # %Y: Year with century (e.g., 2023)
    # %m: Month as a zero-padded decimal number (01-12)
    # %d: Day of the month as a zero-padded decimal number (01-31)
    # %H: Hour (24-hour clock) as a zero-padded decimal number (00-23)
    # %M: Minute as a zero-padded decimal number (00-59)
    # %S: Second as a zero-padded decimal number (00-59)
    formatted_current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f" Current datetime : {formatted_current_date}")

def calculate_future_date():
    """
    Prompts users for a number of days, an integer, then calculate and display futute date after adding those days to the current date
    """

    while True: 
        try:
            # Prompt the user to enter a number of days
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str) # Convert input to an integer
            break # Exit loop if conversion is successful

        except ValueError:
            print("Invalid input. Please enter a whole number for days.")


    current_date_only = datetime.now().date()
    future_date = current_date_only + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"{days_to_add} days from now: {formatted_future_date}")

if __name__ == "__main__":
  display_current_datetime()

  print("\n" + "="*40 + "\n")

  calculate_future_date()