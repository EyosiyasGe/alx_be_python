FAHRENHEIT_TO_CELSIUS_FACTOR = 0
CELSIUS_TO_FAHRENHEIT_FACTOR = 0
x = float(input("enter the amount "))
y= input("Is this temperature in Celsius or Fahrenheit? (C/F) ").lower()
def convert_to_celsius(fahrenheit) :
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = fahrenheit * 5/9
    print(f"{FAHRENHEIT_TO_CELSIUS_FACTOR} C")
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = celsius * 9/5
    print(f"{CELSIUS_TO_FAHRENHEIT_FACTOR} F ")
if y == "c":
    convert_to_fahrenheit(x)
elif y == "f" :
    convert_to_celsius(x)
else :
    print("Invalid temperature. Please enter a numeric value.")