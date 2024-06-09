my_set = {1,2,3,4,5}
your_set ={4,5,6,7,8,9,10}

print(my_set.difference(your_set))  # o/p  {1, 2, 3} print and it will no modify
print(my_set) # {1, 2, 3, 4, 5}

print(my_set.discard(5))  # None
print(my_set)  # {1, 2, 3, 4}

my_set = {1,2,3,4,5}
print(my_set.difference_update(your_set))  # print None  and modify the set
print(my_set)  # {1, 2, 3}

my_set = {1,2,3,4,5}
your_set ={4,5,6,7,8,9,10}
print(my_set.intersection(your_set))  # {4, 5} and will not modify
print(my_set & your_set) # both are same
print(my_set)

print(my_set.isdisjoint(your_set))  # False because 4,5 are common in both the set

print(my_set.union(your_set)) # join both set and avoid reputation {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set | your_set) # both are same

my_set = {4,5}
your_set ={4,5,6,7,8,9,10}
print(my_set.issubset(your_set)) # my_set is inside your_set

print(my_set.issuperset(your_set))  # False
print(your_set.issuperset(my_set))  # True (contains)


