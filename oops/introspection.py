# introspection --> ability to determine the type of the object in run time

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        #  User.__init__(self, email)  # or
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wiz = Wizard('Bredlin', 500, 'bredlinjose@gmail.com')
print(dir(wiz))  # gives all the attributes and method which the wiz instance have (we can able to access with the wiz instance)



