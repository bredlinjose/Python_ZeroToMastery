# tuples are immutable
# we cannot add or modify tuples
# faster than list

numbers = (1, 2, 0, 3, 3, 4, 5)

print(numbers)
print(len(numbers))
print(0 in numbers)
print(numbers.count(3))  # how many times the element present
print(numbers.index(3))  # index of the 1st occurrence of the element

new_tuple = numbers[:]
print(new_tuple)

tuple1 = numbers[1:2]
print(tuple1)  # o/p (2,)

a, b, c, *other = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(other)  # o/p [4, 5, 6, 7]
