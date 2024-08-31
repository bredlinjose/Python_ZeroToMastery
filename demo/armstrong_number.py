import math
def is_armstrong_number(num):
    digits = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        last = temp % 10
        sum += last ** digits
        temp //= 10
    return num == sum


num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

