numb = range(1, 10)
cnt = 0
for number in numb:
    if number % 2 == 0:
        print(number, end=" ")
        cnt += 1

print(end="\n")
print('Even Number Count: ', cnt)

# end=" " --> for space
# end="\n" --> for next line
