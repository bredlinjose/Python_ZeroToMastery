''' Hiding/abstracting the information and giving the access to only necessary '''
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print('running')
        
    def shout(self):
        print(f'My name is {self.name}, I am {self.age} years old')
        
player1 = PlayerCharacter('Bredlin', 27)
print(player1.name)
print(player1.age)
player1.run()
player1.shout()

player1.name = 'Jose'
player1.shout = 'BOOOO'

print( player1.shout)  # BOOOO
print( player1.shout())  # Error 'str' object is not callable
