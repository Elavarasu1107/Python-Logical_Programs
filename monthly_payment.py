import math


def monthly_payment():
    """
    y represents years
    x represents principle
    i represents percent interest
    :return:
    """
    y = int(input("Enter no of years: "))
    x = int(input("Enter principle: "))
    i = int(input("Enter percent interest: "))

    n = 12 * y
    r = i / (12 * 100)
    payment = (x * r) / (1 - math.pow((1 + r), -n))
    print("Monthly payment: ", payment)


if __name__ == '__main__':
    monthly_payment()