
def binary_conversion():
    """
    This function used to convert an integer to a binary value
    :return:
    """
    value = int(input("Enter a value: "))
    binary_value = []
    while value > 0:
        remainder = value % 2
        binary_value.append(remainder)
        value //= 2
    length = len(binary_value) - 1
    i = 0
    while length >= 0:
        print(binary_value[length], end="")
        length -= 1


if __name__ == '__main__':
    binary_conversion()