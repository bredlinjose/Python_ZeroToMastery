# duplicate not allowed
# unordered collection of unique objects
# not index based

my_set ={1,2,3,4,5}
print(my_set)

new_set = {1,2,3,3,4,5,6,8,7,5}
print(new_set)

my_set.add(6)
my_set.add(3)  # duplicate
print(my_set)

my_list = [1,2,3,3,4,5,6,8,7,5]
converted_set = set(my_list)
print(converted_set)

print(len(converted_set))
print(3 in converted_set)

converted_list = list(my_set)
print(converted_list)
