def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)


print(highest_even([3, 7, 8, 10, 11, 15, 14]))
