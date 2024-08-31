def reverse_integer_using_for_loop(num):
    temp = num
    rev = 0
    for i in str(num):
        digit = temp % 10
        rev = (rev*10) + digit
        temp //= 10
    return rev

def reverse_integer_using_while_loop(num):
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = (rev*10) + digit
        temp //= 10
    return rev

def reverse_integer_using_string_slicing(num):
    st = str(num)
    rev = int(st[::-1])
    return rev

def reverse_integer_using_function_call(num):
    li = list(str(num))
    li.reverse()
    rev = int("".join(li))
    return rev


print(reverse_integer_using_for_loop(123))
print(reverse_integer_using_while_loop(123))
print(reverse_integer_using_string_slicing(123))
print(reverse_integer_using_function_call(123))
