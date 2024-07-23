# return will terminate, yield won't terminate

def gen():
    yield 5


value = gen()
print(value)  # <generator object gen at 0x0000021E9BAE4880>
print(value.__next__())  # 5


def gen1():
    yield 1
    yield 3
    yield 5
    yield 7


data = gen1()
print(data.__next__())  # 1
print(data.__next__())  # 3

for i in data:
    print(i)  # 5  # 7
