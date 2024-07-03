# decorator is used to give extra functionality to the function

def my_decorator(func):
    def wrap_func():
        print('*************')
        func()
        print('*************')

    return wrap_func


@my_decorator
def hello():
    print('helllloooooo')


hello()  # same
hello2 = my_decorator(hello)
hello2()  # same
