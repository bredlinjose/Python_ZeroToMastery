class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = m1 + m2
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)  # own implementation


s1 = Student(60, 90)
s2 = Student(50, 70)

print('Sum:', s1+s2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)
# without __str__() -->  <__main__.Student object at 0x000001E18B4EA150>
# with __str__() --> 60 90