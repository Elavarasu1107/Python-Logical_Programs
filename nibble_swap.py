
def nibble_swap():
    """
    This function swap the nibbles in a byte to find corresponding number
    :return:
    """
    value = int(input("Enter a value: "))
    new_value = ((value & 0x0F) << 4 | (value & 0xF0) >> 4)
    print("Value after swapping nibbles: ", new_value)


if __name__ == '__main__':
    nibble_swap()