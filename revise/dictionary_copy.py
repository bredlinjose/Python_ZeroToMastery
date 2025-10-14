
dict1 = {"a": 1, "b": 2}
dict2 = dict1  # Same Object (Reference)  # Both variables point to the same dictionary (a reference)

dict2["a"] = 100

print(dict1)  # {'a': 100, 'b': 2}


dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()  #  Shallow Copy  # creates a new dictionary with the same keys and values. They are now separate.

dict2["a"] = 100

print(dict1)  # {'a': 1, 'b': 2}
print(dict2)  # {'a': 100, 'b': 2}

# If your dictionary contains nested dictionaries or lists, .copy() copies only the top level — not the inner objects.
dict1 = {"a": 1, "b": {"x": 10}}
dict2 = dict1.copy()

dict2["b"]["x"] = 999

print(dict1)  # {'a': 1, 'b': {'x': 999}}  # change did in dict2 but also changed in dict2




# dict1 = {"a": 1, "b": {"x": 10}}
# dict2 = copy.deepcopy(dict1)  # import copy  # copy.deepcopy() when you want to copy everything, including nested structures
#
# dict2["b"]["x"] = 999
#
# print(dict1)  # {'a': 1, 'b': {'x': 10}}  # not changed
