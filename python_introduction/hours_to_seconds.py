# hours_to_seconds.py

# Define the variable for the number of hours
hours = 2

# Calculate the number of seconds in the given hours
# 1 hour = 60 minutes
# 1 minute = 60 seconds
# So, 1 hour = 60 * 60 = 3600 seconds
seconds = hours * 3600

# Print the result in the specified format
# We use an f-string for easy formatting.
# Note: Using "hour(s)" to correctly display "hour" for 1 and "hours" for others.
print(f"{hours} hour(s) is {seconds} seconds")