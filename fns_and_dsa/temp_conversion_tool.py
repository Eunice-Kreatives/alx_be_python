# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    while True: 
        try:
            temperature = float(input("Enter the temperature to convert: ").strip())
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C' , 'F']:
            break
        else:
            print("Error. Input a valid unit") 
    if unit == 'C':
        converted_temperature = convert_to_celsius(temperature)
        print (f"{temperature}°C is {converted_temperature}°F")
    elif unit == 'F':
        converted_temperature = convert_to_fahrenheit(temperature)
        print (f"{temperature}°F is {converted_temperature}°C")

if __name__ == "__main__" :
    main()
    
