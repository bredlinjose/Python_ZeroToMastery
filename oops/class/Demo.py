
class Data:
    company = 'UTH UK'  # static variable

    def __init__(self):
        self.name = 'Bredlin'  # instance variable
        self.age = 27

    def update(self):
        self.age = 50

    def compare(self, other):
        return self.age == other.age


d1 = Data()
print(d1.age)
d1.age = 25
print(d1.age)

d2 = Data()
print(d2.name)
print(d2.age)
d2.update()
print(d2.age)

if d1.compare(d2):
    print("Same age")
else:
    print("Different age")

print(d1.company)
print(d2.company)
print(Data.company)

Data.company = 'Google'
print(d1.company)
print(d2.company)
print(Data.company)

