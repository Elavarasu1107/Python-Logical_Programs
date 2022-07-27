
def perfect_number():
    """
    This function used to find whether given number is perfect number
    :return: 
    """
    number = int(input("Enter a Number: "))
    temp = 0
    if number % 2 == 0:
        i = 1
        while i < number:
            if number % i == 0:
                temp += i
            i += 1
        if temp == number:
            print("Entered Number ", number, " is a Perfect Number")
        else:
            print("Entered Number ", number, " is not a Perfect Number")
    else:
        print("Entered Number ", number, " is not a Perfect Number")


if __name__ == '__main__':
    perfect_number()
