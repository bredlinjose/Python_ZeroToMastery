# move all the '-' last
st = "hypen-of-hello"


def move_hypen(word):
    count = 0
    result = ""
    for ch in st:
        if ch != "-":
            result += ch
        else:
            count += 1

    return result + count * "-"


output = move_hypen(st)
print(output)
