user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 26
}
print('age' in user)  # True
print(26 in user)  # False --> it will check only the key

print('age' in user.keys())
print(26 in user.values())
print(user.items())  # print as tuples

user2 = user.copy()
print(user2)
print(user)

user2.clear()
print(user2)

print(user.pop('age'))  # remove the element and print the value
print(user)

print(user.popitem())  # remove the random elements
print(user)

print(user.update({'ages': 24}))  # if it is not there then add
print(user)

print(user.update({'ages': 26}))  # if it is there then update
print(user)
