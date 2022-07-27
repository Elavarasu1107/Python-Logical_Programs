
def prime_number():
    value = int(input("Enter a Number: "))
    temp = 0
    if value >= 2:
        i = 2
        while i < value:
            if value % i == 0:
                temp += 1
            if temp >= 1:
                break
            i += 1
        if temp == 0:
            print("Entered Number ", value, " is a Prime Number")
        else:
            print("Entered Number ", value, " is not a Prime Number")


if __name__ == '__main__':
    prime_number()