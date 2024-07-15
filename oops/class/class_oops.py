class BigObject:  # class
    pass


obj1 = BigObject()  # instanciate
obj2 = BigObject()  # instanciate

print(type(obj1))  # <class '__main__.BigObject'>
print(id(obj1))  # print the address of the instance in the heap memory
print(type(obj2))  # <class '__main__.BigObject'>
print(id(obj2))  # print the address of the instance in the heap memory

class Computer:
    def __init__(self, processor, ram):
        print('inside __init__')
        self.processor = processor
        self.ram = ram

    def config(self):
        print('Processor:', self.processor)
        print('RAM:', self.ram)


com1 = Computer('Intel i5', '16gb')
com1.config()

com2 = Computer('Rayzen 5', '8gb')
com2.config()

