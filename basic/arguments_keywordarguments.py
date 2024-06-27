def super_func(*args):
    print(args)  # tuple
    return sum(args)


print(super_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def super_func1(**kwargs):
    print(kwargs)  # dictionary
    total = 0
    for item in kwargs.values():
        total += item
    return total


print(super_func1(num1=5, num2=10))


def super_func2(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(super_func2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, num1=5, num2=10))

# Rules: def function_name(param, *args, default param, **kwargs)
# Ex: def fun(name, *args, i=3, **kwargs)
