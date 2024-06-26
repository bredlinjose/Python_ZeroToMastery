my_list = [1, 2, 3, 4, 5]

for num in my_list:
    print(num)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('say something: ')
    if response == 'bye':
        break

for num in my_list:
    continue
    print(num)  # it wont print

for num in my_list:
    # thinking about it
    pass
