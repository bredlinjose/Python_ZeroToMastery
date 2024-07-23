def fibonacci(num):
    a = 0
    b = 1
    print(a, end=' ')
    print(b, end=' ')
    for i in range(2, num):
        c = a + b
        print(c, end=' ')
        a = b
        b = c
    print()

def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


no = 10
fibonacci(no)

for i in range(10):
    print(fib(i), end=' ')
