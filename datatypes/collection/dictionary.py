# dict key value can be unique
# allow tuple as key not allow list as key
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(dictionary)
print(dictionary['a'])

dictionary1 = {
    'a': ['a', 'b', 'c'],
    'b': True,
    'c': "hello"
}
print(dictionary1)
print(dictionary1['a'][2])
# print(dictionary1['d']) not present so error
print(dictionary1.get('d'))  # o/p None
print(dictionary1.get('d', 'bro'))  # if d is present in the dict then it will print that otherwise bro

my_list = [
    {
        'a': [1, 2, 3],
        'b': True,
        'c': "hello"
    },
    {
        'a': [4, 5, 6],
        'b': False,
        'c': "hii"
    }
]
print(my_list[0])
print(my_list[0]['a'])
print(my_list[0]['a'][2])

# new_basket = dict('name'= 'Bredlin') # error in key
new_basket = dict(name='Bredlin', age=26)
print(new_basket)
