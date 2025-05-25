# finance_calculator.py

# --- User Input for Financial Details ---

# Prompt the user for their monthly income.
# We use float() to convert the input text into a number that can have decimals,
# which is common for money.
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# --- Calculate Monthly Savings ---

# Subtract expenses from income to find monthly savings.
monthly_savings = monthly_income - monthly_expenses

# --- Project Annual Savings with Interest ---

# Define the annual interest rate as a decimal.
annual_interest_rate = 0.05 # Represents 5%

# Calculate projected savings after one year.
# Formula: (Monthly Savings * 12) + (Monthly Savings * 12 * Interest Rate)
# This can be simplified to: Monthly Savings * 12 * (1 + Interest Rate)
projected_annual_savings = monthly_savings * 12 * (1 + annual_interest_rate)

# --- Output Results ---

# Display the user's monthly savings.
# We use an f-string for easy formatting.
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f formats to 2 decimal places

# Display the projected annual savings, including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")