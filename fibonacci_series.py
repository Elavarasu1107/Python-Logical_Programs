def fibonacci_series():
    """
    This function used to generate fibonacci series upto n
    :return:
    """
    n = int(input("Enter the value of n: "))
    series = list()
    i = 0
    while i < n:
        if i == 0 or i == 1:
            series.append(i)
        else:
            series.append(series[i - 2] + series[i - 1])
        i += 1
    print(series)


if __name__ == '__main__':
    fibonacci_series()
