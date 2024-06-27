def is_prime(num):
    count = 0
    for n in range(1, num + 1):
        if num % n == 0:
            count = count + 1
    if count == 2:
        return str(num) + ' is a prime number'
    else:
        return str(num) + ' is not a prime number'


print(is_prime(1))

number = 4
for num in range(2, number):
    if number % num == 0:
        print(number, 'is not a prime number')
        break
else:
    print(number, 'is a prime number')
