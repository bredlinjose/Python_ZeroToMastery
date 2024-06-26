# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")
# # or
# for number in range(1, 4):
#     print("Attempt", number, number * ".")

successful = False
for number in range(3):
    print("Attempt", number+1)  # index, so +1
    if successful:
        print("Passed")
        break
else:
    print("Attempted 3 times and failed")
