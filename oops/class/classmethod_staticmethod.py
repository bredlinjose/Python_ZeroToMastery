class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def shout(self):
        print(f'my name issss {self.name}')

    # class method and static method are similar the only change is
    # in class method we will use cls
    # in static method we dont have access to the parameter cls, we wont care about the class state

    @classmethod  # Its similar to static method in java, without instanciate also we acn use with the help of class name
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def dummy(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def addition(num1, num2):
        return num1 + num2

print('Addition:', PlayerCharacter.adding_things(2, 4))

print(PlayerCharacter.dummy(3, 6))  # <__main__.PlayerCharacter object at 0x0000021D46C59DF0>



player = PlayerCharacter('Bredlin', 27)
player.shout()
