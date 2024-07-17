class Student:  # outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:  # inner class
        def __init__(self):
            self.brand = "Realme"
            self.processor = "i5"
            self.ram = 16

        def show(self):
            print(self.brand, self.processor, self.ram)


s1 = Student('Bredlin', 1)
s2 = Student('Jose', 2)

print(s1.lap.brand)
print(s1.lap.ram)

lap1 = s1.lap
lap2 = s2.lap
print(lap1.brand)
print(lap2.processor)

lap = Student.Laptop()
print(lap.processor)

s1.show()
