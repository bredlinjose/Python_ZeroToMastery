selfish = 'me me me'
print(selfish[1])

selfish = '1234567'  # reinitialization
print(selfish[1:6])  # from index 1 to 6 excluding 6
# [start : stop : step-over] --> String slicing
print(selfish[0:4])  # by default step-over is 1
print(selfish[1:6:2])
print(selfish[:6])  # by default, it will start from beginning
print(selfish[1:])  # by default, it will stop at last
print(selfish[:])  # by default, it will start from beginning and stop at last
print(selfish[::])  # by default, it will start from beginning ,stop at last and step-over 1

print(selfish[-2])  # -value will take from the last

print(selfish[::-1])  # reverse
print(selfish[::-2])
