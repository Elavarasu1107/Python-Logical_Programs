import random


def coupon_number():
    """
    This function used to generate distinct coupon numbers
    :return:
    """
    value = int(input("Enter number of coupons to Generate: "))
    coupon_list = []
    i = 0
    total_random_numbers = 0
    while i < value:
        coupon = random.randint(10, 99)
        list_checker = 0
        if len(coupon_list) != 0:
            j = 0
            while j < i:
                if coupon_list[j] == coupon:
                    list_checker = 1
                    break
                j += 1
        if list_checker != 1:
            coupon_list.append(coupon)
        else:
            i -= 1
        i += 1
        total_random_numbers += 1

    print(coupon_list)
    print("Total numbers to have all distinct coupons: ", total_random_numbers)


if __name__ == '__main__':
    coupon_number()

