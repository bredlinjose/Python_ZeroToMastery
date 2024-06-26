# string accept both "" and ''
username = 'Bredlin'
password = "bredlin123"

print(username)
print(password)
print(type(username))

# ''' multiline string
uff = '''WOW
0 0
---'''
print(uff)

# string is immutable
selfish = 'you you you'
# selfish[0] = 'h'
# # TypeError: 'str' object does not support item assignment
selfish = selfish + ' me'
print(selfish)

first_name = 'Bredlin'
last_name = 'Jose'
full_name = first_name + ' ' + last_name
print(full_name)

text = "The best things in life are free!"
print("free" in text)
txt = "The best things in life are free!"
print("expensive" not in txt)
