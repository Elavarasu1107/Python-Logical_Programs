
def week_days():
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day = int(input("Enter a Date: "))
    month = int(input("Enter a Month: "))
    year = int(input("Enter a Year: "))

    y = year - (14 - month) // 12
    x = y + y // 4 - y // 100 + y // 400
    m = month + 12 * ((14 - month) // 12) - 2
    d = (day + x + (31 * m) // 12) % 7

    print("It's ", week_days[d])


if __name__ == '__main__':
    week_days()
