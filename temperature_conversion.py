# Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales. 
# The program should prompt the user to input a temperature value and the original unit of measurement. 
# It should then convert the temperature to the other two units
# and display The converted values tothe user. 
# For example, if the user enters a temperature of 25 degrees Celsius, the program should convert it to Fahrenheit and Kelvin,
# and present the converted values as outputs.

# function to convert from celsius to Fahrenheit and Kelvin
def celsius_to_fahrenheit_and_kelvin(celsius):
    # the formula °F = °C * 9/5 + 32 to convert C to F
    fahrenheit = celsius * (9/5) + 32
    # rounding of 2 decimal
    fahrenheit = round(fahrenheit,2)
    #  K = °C + 273.15
    kelvin = celsius + 273.15
    # rounding of 2 decimals
    kelvin = round(kelvin,2)
    return fahrenheit, kelvin

def fahrenheit_to_celsius_and_kelvin(fahrenheit):
    # Formula °C = (°F − 32) × 5/9
    celsius = (fahrenheit - 32) * (5/9)
    celsius = round(celsius,2)
    #  K = (°F + 459.67) × 5/9
    kelvin = (fahrenheit + 459.67) *(5/9)
    kelvin = round(kelvin,2)
    return celsius, kelvin

def kelvin_to_celsius_and_fahrenheit(kelvin):
    # Formula °C = K − 273.15
    celsius = kelvin - 273.15
    celsius = round(celsius,2)
    # °F = K × 9/5 − 459.67
    fahrenheit = kelvin * (9/5) - 459.67
    fahrenheit = round(fahrenheit,2)
    return celsius, fahrenheit


def main():
    try:
        temperature = float(input("Enter the temperature value: "))
        units = input("Enter units of the temperature (clesius - c or fahreinheit - f or kelvin - k): ").strip().lower()

        if units == "c":
            fahrenheit, kelvin = celsius_to_fahrenheit_and_kelvin(temperature)
            print(f"Temperature {temperature} \u00B0C is equal to {fahrenheit} \u00B0F or {kelvin} K.")
        elif units == 'f':
            celsius, kelvin = fahrenheit_to_celsius_and_kelvin(temperature)
            print(f"Temperature {temperature} \u00B0F is equal to {celsius} \u00B0C or {kelvin} K.")
        elif units == 'k':
            celsius, fahrenheit = kelvin_to_celsius_and_fahrenheit(temperature)
            print(f"Temperature {temperature} K is equal to {celsius} \u00B0C or {fahrenheit} \u00B0F.")
        else:
            raise ValueError("Invalid unit!!!.Try Again")

    except ValueError as err:
        print(f"Invalid input for temperature!!! : \n{err}")



if __name__ == "__main__":
    while True:
        main()
        should_continue = input("You want to convert again for other temperature (yes or no): ").strip().lower()
        if should_continue =="no":
            print("Bye!!!")
            break
        elif should_continue != "yes":
            print("That's an incorrect option!!!")
            break