my_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

# without set
duplicate = []
for value in my_list:
    if my_list .count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)