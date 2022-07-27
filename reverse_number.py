
def reverse_number():
    value = int(input("Enter a Number: "))
    reverse_value = 0

    while value > 0:
        remainder = value % 10
        reverse_value = (reverse_value * 10) + remainder
        value = value // 10
    print("Reverse Number of a value: ", reverse_value)


if __name__ == '__main__':
    reverse_number()
