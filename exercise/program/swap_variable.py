def swap_number1():
    a = 10
    b = 20
    temp = a
    a = b
    b = temp
    print("a:", a)
    print("b:", b)

def swap_number2():
    a = 10
    b = 20
    b = b - a
    a = a + b
    print("a:", a)
    print("b:", b)


swap_number1()
swap_number2()
