# there is no concept of method overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(100, 90)
print(s1.sum(10, 20, 30))
print(s1.sum(10, 20))
print(s1.sum(10))


def addition(*args):
    return sum(args)


print(addition(2, 3))
print(addition(2, 3, 4))
print(addition(2, 3, 4, 5))

