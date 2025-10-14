def find_duplicate_character_frequency(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # print(char_count)  # count of all the character

    duplicate_char = {}
    for char, count in char_count.items():
        if count > 1:
            duplicate_char[char] = count

    print(duplicate_char)  # only duplicate and its count


def find_duplicates(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        if count > 1:
            print(f"{char}: {count}")


word = "programmer"
find_duplicate_character_frequency(word)
find_duplicates(word)
