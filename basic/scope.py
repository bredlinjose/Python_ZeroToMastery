num = 100  # global
if True:
    x = 99


def some_func():
    total = 1500  # local
    print(total)


some_func()

# print(total)  # error bcz total is local to the some_func()

print(x)

a = 1


def confusion():
    a = 5
    return a


print(a)  # 1
print(confusion())  # 5


def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())  # 10


a1 = 10


def confusion(b):
    print(b)
    a1 = 90


confusion(20)
