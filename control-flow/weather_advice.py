
# weather_advice.py

# Prompt User for Weather Input
# Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
# Use the prompt: What's the weather like today? (sunny/rainy/cold):
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower() # .lower() converts input to lowercase for case-insensitive comparison

# Provide Clothing Recommendations
# Based on the user’s input, your program will recommend different types of clothing:
# If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
# If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.
else:
    print("Sorry, I don't have recommendations for this weather.")