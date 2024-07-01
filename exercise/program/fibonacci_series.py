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


fibonacci(10)
