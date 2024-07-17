from abc import ABC, abstractmethod
# ABC --> Abstract Base Class
class Computer(ABC):
    @abstractmethod
    def processor(self):
        pass

class Laptop(Computer):
    def processor(self):
        print("its running")

class Programmer:
    def work(self, com):
        print("Fixing Bugs")
        com.processor()

com1 = Laptop()

prog = Programmer()
prog.work(com1)
