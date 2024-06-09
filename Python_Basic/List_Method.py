numbers = [1, 2, 3, 4, 5]
print(numbers)

new_numbers = numbers.append(6)
print(new_numbers)  # None --> it will not return any value

# numbers.append(6)
print(numbers)

numbers.extend([100,101])
print(numbers)

numbers.remove(6) # remove the mentioned element, it will not return any value
print(numbers)

numbers.pop()  # remove the last element
numbers.pop(0)  # remove the element from the mentioned index

list1 = numbers.pop(2)  # it will return value
print(list1)

numbers.insert(0, -1)
print(numbers)

print(3 in numbers) # checks the number is present or not

print(len(numbers))

numbers.clear()
print(numbers)

basket =['a','b','c','d','b','e','f']
print(basket.index('b')) # print the 1st index
#print(basket.index('d',0,2))  # looks for the particular element in the mentioned index if not there error
print(basket.count('b'))

print(basket.sort())  # None  --> will not return any value
basket.sort()
print(basket)

print(sorted(basket))  # create a copy

basket.reverse()
print(basket)

print(list(range(100)))

sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'bredlin'])  # it will return value
print(sentence)  # !
print(new_sentence)