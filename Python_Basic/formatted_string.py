name = 'Bredlin'
age = 26

print('Hi '+name+'. You are '+str(age)+' years old') #normal

print(f'Hi {name}. You are {age} years old') # formatted string--> f(from python 3)

# format() --> python 2
print('Hi {}. You are {} years old'.format("Jose","27"))

print('Hi {}. You are {} years old'.format(name,age))

print('Hi {1}. You are {0} years old'.format(name,age))

# print('Hi {0}. You are {1} years old'.format(new_name='Deeps',age=22))
# exception: IndexError: Replacement index 0 out of range for positional args tuple

print('Hi {new_name}. You are {age} years old'.format(new_name='Deeps',age=22))





