def say_hello():
    print("Hello")


say_hello  # nothing will happen bracket missing
say_hello()  # calling function


# show_tree()  # error interpreter line by line execution (defined below)


def show_tree():
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]
    for image in picture:
        for pixel in image:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


show_tree()
print(show_tree)  # <function show_tree at 0x000001A9E65D4AE0>  # location in memory
