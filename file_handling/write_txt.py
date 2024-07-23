r = open("notes.txt", "r")

w = open("dummy.txt", "w")  # if file is not present it will create
w.write("Something ")  # Something
w.write("People ")  # Something People

w = open("dummy.txt", "a")  # append
w.write("Laptop ")  # Something People Laptop
w.write("Mobile  ")

for data in r:
    w.write(data)
