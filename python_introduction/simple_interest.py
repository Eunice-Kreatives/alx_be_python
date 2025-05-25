# simple_interest.py

# Define the variables for simple interest calculation
# P = Principal amount (initial investment)
principal = 1000

# R = Annual interest rate (as a decimal)
rate = 0.05

# T = Time the money is invested for in years
time = 3

# Calculate the simple interest using the formula I = P * R * T
# The result will be stored in the 'interest' variable
interest = principal * rate * time

# Print the calculated interest in the specified format
# We use an f-string to easily include the 'interest' variable's value
print(f"The simple interest is: {interest}")