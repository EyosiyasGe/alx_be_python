FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit) :
     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
try :
    x = float(input("enter the amount "))
    y= input("Is this temperature in Celsius or Fahrenheit? (C/F) ").lower()
    if y == "c":
        print(convert_to_fahrenheit(x))
    elif y == "f" :
        print(convert_to_celsius(x))
    else :
        print("Invalid temperature. Please enter a numeric value.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")