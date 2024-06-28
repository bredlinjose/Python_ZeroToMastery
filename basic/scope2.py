total = 0


# def count1():
#     total += 1  # error bcz total is not belong to the count1()
#     return total

def count2():
    total = 0
    total += 1
    return total


print(count2())

# global keyword
# def count1():
#     global total  # not a good practice
#     total += 1
#     return total
#
# print(count1())

def count1(total):
    total += 1
    return total

print(count1(total))
print(count1(count1(count1(total))))

# nonlocal keyword
def outer_func():
    x = 'local'
    def inner_func():
        nonlocal x  # we are re-assigning the parent x
        x = 'nonlocal'
        print('inner:', x)
    inner_func()
    print('outer:', x)


