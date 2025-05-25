# future_age_calculator.py

# Prompt the user to input their current age
# The input() function gets text from the user.
# The int() function converts that text into a whole number (integer).
current_age = int(input("How old are you? "))

# Define the target year and the assumed current year
current_year = 2023
future_year = 2050

# Calculate the number of years between the current year and the future year
years_to_add = future_year - current_year # This will be 2050 - 2023 = 27

# Calculate the user's age in the future year
future_age = current_age + years_to_add

# Print the result in the specified format using an f-string
print(f"In {future_year}, you will be {future_age} years old.")