numbers = [12, 14, 16, 21, 7, 11]
# check the number which is divisible by 5

divisible_by = 5
for num in numbers:
    if num % divisible_by == 0:
        print(num, 'is divisible by '+str(divisible_by))
        break
else:
    print('not found')
