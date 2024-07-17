nums = [5, 6, 7, 8, 9]

it = iter(nums)
print(it)

print(it.__next__())  # 5
print(it.__next__())  # 6
print(next(it))  # same  # 7


