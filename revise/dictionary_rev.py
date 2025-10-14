student = {"first_name": "Bredlin", "last_name": "Jose", "age": 28}

print(student.items())  # <class 'dict_items'>  # Returns all key-value pairs as tuples
# dict_items([('first_name', 'Bredlin'), ('last_name', 'Jose'), ('age', 28)])

print(student.values())  # <class 'dict_values'>  # Returns all values
# dict_values(['Bredlin', 'Jose', 28])
print(student.keys())  # <class 'dict_keys'>  # Returns all keys
# dict_keys(['first_name', 'last_name', 'age'])

print(list(student.keys()))  # Returns all keys as list # ['first_name', 'last_name', 'age']
print(list(student))  # Returns all keys as list # ['first_name', 'last_name', 'age']

# add
student["last_name"] = "T"
student["course"] = "Python"

# update
student["age"] = 25
print(student)  # {'first_name': 'Bredlin', 'last_name': 'T', 'age': 25, 'course': 'Python'}
s1 = {"id": 100, "address": "Bengaluru"}
student.update(s1)  # if the key is not there then it will add, if not update
print(student)  # {'first_name': 'Bredlin', 'last_name': 'T', 'age': 25, 'course': 'Python', 'id': 100, 'address': 'Bengaluru'}

# access
print(student["first_name"])  # Bredlin
print(student.get("first_name"))  # Bredlin
print(student.get("location"))  # None  # location key is not there in the dict  # No error
# print(student["location"])  # KeyError  # location key is not there in the dict  # Error
print(student.get("location", "Invalid key"))  # Invalid key  # if the key is not present then return the default value mentioned

# delete
del student["course"]  # Deletes the key 'course'
print(student)  # {'first_name': 'Bredlin', 'last_name': 'T', 'age': 25, 'id': 100, 'address': 'Bengaluru'}

rem = student.pop("age")  # Removes and returns 'age'
print(rem)  # 25
print(student)  # {'first_name': 'Bredlin', 'last_name': 'T', 'id': 100, 'address': 'Bengaluru'}
student.clear()  # Clears all key-value pairs
print(student)  # {}


#  Looping Through Dictionary
student = {'first_name': 'Bredlin', 'last_name': 'T', 'age': 25, 'course': 'Python', 'id': 100, 'address': 'Bengaluru'}
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, "->", value)
