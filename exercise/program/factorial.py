def factorial(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


nu = 5
print(factorial(nu))
print(fact(nu))
