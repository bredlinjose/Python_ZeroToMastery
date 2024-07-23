def perfect_square(num):
    n = 1
    while n <= num:
        sq = n*n
        yield sq
        n += 1


value = perfect_square(10)
for i in value:
    print(i)
