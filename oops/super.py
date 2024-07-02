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
wiz.sign_in()
wiz.attack()

print(wiz.email)
