
def vending_machine():
    """
    This function returns change of cash for the given input
    :return:
    """
    amount = int(input("Enter a Amount: "))
    available_notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    change = []
    for i in range(0, len(available_notes)):
        if amount >= available_notes[i]:
            change.append(amount // available_notes[i])
            amount = amount - (change[i] * available_notes[i])
        i += 1
    print("Change for an Entered Amount: ")
    for j in range(0, len(change)):
        print(available_notes[j], " Notes are: ", change[j])
        j += 1


if __name__ == '__main__':
    vending_machine()
