names = ["Bredlin", "Josh", "Sara", "Deeps", "Caffrey"]
print(names)

names[1] = "Jose"
print(names)

print(names[0])
print(names[-1])  # from last
print(names[-2])

print(names[1:3])  # print 1,2 index value

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

a, b, c, *other, d = [1.0, 2.0, 3.0, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)