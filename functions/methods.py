class Student:
    school = 'ABC Hr Sec School'  # class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1  # instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance method (self)
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):  # accessor method
        return self.m1

    def set_m1(self, value):  # mutator method
        self.m1 = value

    @classmethod
    def get_school(cls):  # class method (cls)
        return cls.school

    @staticmethod
    def info():  # static method ()
        return 'This is a Student class'


s1 = Student(98, 99, 97)
s2 = Student(36, 38, 36)
print(s1.avg())

print(Student.get_school())
print(Student.info())

