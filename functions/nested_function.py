# def add(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#
# print(add(1, 3))  # None

# def add(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#     return another_func
#
# print(add(1, 2))  # <function add.<locals>.another_func at 0x000001E0565249A0>

def add(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


print(add(1, 2))
