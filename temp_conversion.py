# Temperature Conversion Program

temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C / F / K): ")

if unit == 'C' or unit == 'c':
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("Temperature in Fahrenheit:", fahrenheit)
    print("Temperature in Kelvin:", kelvin)

elif unit == 'F' or unit == 'f':
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("Temperature in Celsius:", celsius)
    print("Temperature in Kelvin:", kelvin)

elif unit == 'K' or unit == 'k':
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Celsius:", celsius)
    print("Temperature in Fahrenheit:", fahrenheit)

else:
    print("Invalid unit! Please enter C, F, or K.")
