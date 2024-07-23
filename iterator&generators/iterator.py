nums = [5, 6, 7, 8, 9]

it = iter(nums)
print(it)  # <list_iterator object at 0x00000199744D7F40>

print(it.__next__())  # 5
print(it.__next__())  # 6
print(next(it))  # same  # 7

for i in it:
    print(i)  # 8  # 9


