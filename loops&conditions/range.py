numbers = range(5)  # 0 to 5 excluding 5(sequence of numbers)
print(numbers)  # range(5)
for num in numbers:
    print(num)

num1 = range(5, 10)  # 5 to 10 excluding 10(sequence of numbers)
print(num1)  # range(5, 10)
for num in num1:
    print(num)

num2 = range(5, 10, 2)  # 5 to 10 and jump 2 and excluding 10(sequence of numbers)
print(num2)  # range(5, 10, 2)
for num in num2:
    print(num)

for num in range(3, 15, 3):
    print(num)
