# functions act like a variable
# decorators supercharge function

def hello():
    print('hellloooooo')


# greet = hello()
# print(greet)

greet = hello
print(greet())

# del hello
# hello()  # NameError: name 'hello' is not defined


def hai(func):
    func()


def wish():
    print('Happy Birthday')


a = hai(wish())
print(a)
