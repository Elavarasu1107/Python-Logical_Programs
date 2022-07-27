
def temperature_converter():
    """
    This function is used to calculate celsius and fahrenheit
    :return:
    """
    try:
        value = int(input("Enter a value to Convert: "))
        fahrenheit = (value * 9 / 5) + 32
        celsius = (value - 32) * 5 / 9
        print("Fahrenheit: ", fahrenheit)
        print("Celsius: ", celsius)
    except ValueError:
        print("Invalid Input")


if __name__ == '__main__':
    temperature_converter()
    