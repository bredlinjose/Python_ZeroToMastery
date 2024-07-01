class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'My name is {self.name}, I am {self.age} years old')

    def say_hai(self):
        print('Haii')

std = Student('bredlin', '27')
std.speak()
std.say_hai()