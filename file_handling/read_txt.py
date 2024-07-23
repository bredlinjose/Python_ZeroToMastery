f = open("notes.txt", "r")

print(f)  # <_io.TextIOWrapper name='notes.txt' mode='r' encoding='cp1252'>
# print(f.read())  # whole content

print(f.readline(), end='')  # 1st line
print(f.readline(), end='')  # 2nd line

print(f.readline(5), end='')  # fetch 5 character
