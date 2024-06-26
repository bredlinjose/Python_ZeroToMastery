for i, char in enumerate('Hello'):  # gives index also
    print(i, char)

for i, char in enumerate([1, 2, 3, 4, 5, 6]):
    print(i, char)

for i, char in enumerate((1, 2, 3, 4, 5, 6, 7)):  # gives index also
    print(i, char)

for i, c in enumerate(list(range(100))):  # index of value 50
    if c == 50:
        print(f'index of 50 is: {i}')
