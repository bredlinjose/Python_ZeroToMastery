letters =["a", "b", "c", "d"]

i = 0
while i< len(letters):
    print(letters[i])
    i = i+1

for letter in letters:
    print(letter)

for letter in enumerate(letters): # enumerate will print as tuples (index, value of index)
    print(letter)

for letter in enumerate(letters):
    print(letter[0], letter[1]) # letter[0] -- tuples index and # letter[1] -- tuples index value

# unpacking tuple
for index, letter in enumerate(letters): # enumerate will return tuples (index, value of index) that we are storing in index, letter
    print(index, letter)
