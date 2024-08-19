import math


def check_armstrong(num):
    temp = num
    digit = math.floor((math.log10(temp) + 1))
    sum = 0
    while temp > 0:
        last = temp % 10
        sum += int(math.pow(last, digit))
        temp //= 10

    if num == sum:
        print(f"Given number {num} is an Armstrong")
    else:
        print(f"Given number {num} is not an Armstrong")


check_armstrong(0)

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

# check_armstrong(0)
