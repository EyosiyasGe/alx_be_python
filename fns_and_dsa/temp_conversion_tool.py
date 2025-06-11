FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
x = float(input("enter the amount "))
y= input("Is this temperature in Celsius or Fahrenheit? (C/F) ").lower()
def convert_to_celsius(fahrenheit) :
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    fahrenheit = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    celsius = celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius
if y == "c":
    print(convert_to_fahrenheit(x))
elif y == "f" :
    print(convert_to_celsius(x))
else :
    print("Invalid temperature. Please enter a numeric value.")