def is_armstrong(num: int) -> bool:
    temp = num
    # digits = str(num).__len__()
    digits = len(str(num))
    result = 0
    print("No. of digits", digits)
    while temp > 0:
        rem = temp % 10
        # result += pow(rem, digits)
        result += rem ** digits
        temp //= 10

    # if result == num:
    #     return True
    # else:
    #     return False
    return result == num


if is_armstrong(153):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")