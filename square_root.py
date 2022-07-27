
def square_root():
    """
    This function used to find a square root of a number
    :return:
    """
    value = int(input("Enter a Value: "))
    temp = value
    while abs(temp - value / temp) > ((1 * 10**-15) * temp):
        temp = ((value / temp) + temp) / 2
    print("Square root of ", value, " is: ", temp)


if __name__ == '__main__':
    square_root()
