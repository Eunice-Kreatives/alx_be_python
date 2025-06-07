# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # (Fahrenheit - 32) * 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # (Celsius * 9/5) + 32

def convert_to_celsius(fahrenheit):
  """
  Converts a temperature from Fahrenheit to Celsius.

  Args:
    fahrenheit (float): The temperature in Fahrenheit.

  Returns:
    float: The temperature converted to Celsius.
  """
  
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """
  Converts a temperature from Celsius to Fahrenheit.

  Args:
    celsius (float): The temperature in Celsius.

  Returns:
    float: The temperature converted to Fahrenheit.
  """

  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """
  Prompts the user for a temperature and unit, performs the conversion,
  and displays the result. Handles input validation.
  """
  print("--- Temperature Conversion Tool ---")

  while True:
    temperature_str = input("Enter the temperature value: ").strip()
    try:
      temperature = float(temperature_str) 
      break 
    except ValueError:
      # Raise a ValueError if the input is not numeric
      print("Invalid temperature. Please enter a numeric value.")
      # Continue the loop to prompt for input again
      continue

  while True:
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    if unit in ['C', 'F']:
      break # Exit loop if unit is valid
    else:
      print("Invalid unit. Please enter 'C' or 'F'.")

  # Perform the conversion based on the user's input unit
  if unit == 'C':
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temperature:}°F")
  elif unit == 'F':
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temperature:}°C")


if __name__ == "__main__":
  main()
