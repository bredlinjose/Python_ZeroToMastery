class Toy:
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }


# act = Toy('Red', 1)
# print(act.__str__())  # <__main__.Toy object at 0x000001C97E7496A0>
# print(str(act))   # <__main__.Toy object at 0x000001C97E7496A0>

    def __str__(self):  # similar like overriding the object clss method and giving our own implementation
        return f'{self.colour}'

    def __len__(self):
        return 5

    def __call__(self):  # call the instance
        return 'yess?'

    def __getitem__(self, item):
        return self.my_dict[item]


act = Toy('Red', 1)
print(act.__str__())  # Red
print(str(act))  # Red
print(len(act))  # 5
print(act())  # yess? (__call__)
print(act['name'])  # Yoyo (__getitem__)

