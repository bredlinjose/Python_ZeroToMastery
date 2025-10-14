#  string is immutable
#  All string methods returns new values.
#  They do not change the original string.

word = "my name is Bredlin Jose"
print(word)

# Case Conversion:
# upper(): Converts all characters in the string to uppercase.
# lower(): Converts all characters in the string to lowercase.
# capitalize(): Converts the first character to uppercase and the rest to lowercase.
# title(): Converts the first character of each word to uppercase.
# swapcase(): Swaps the case of all characters (uppercase to lowercase, lowercase to uppercase).

print(word.upper())  # MY NAME IS BREDLIN JOSE
print(word.lower())  # my name is bredlin jose
print(word.capitalize())  # My name is bredlin jose
print(word.title())  # My Name Is Bredlin Jose
print(word.swapcase())  # MY NAME IS bREDLIN jOSE

# Searching and Finding:
# find(substring): Returns the lowest index where the substring is found, or -1 if not found.
# index(substring): Similar to find(), but raises a ValueError if the substring is not found.
# count(substring): Returns the number of non-overlapping occurrences of the substring.
# startswith(prefix): Checks if the string starts with the specified prefix.
# endswith(suffix): Checks if the string ends with the specified suffix.

name = "bredlin jose"
print(name.find("o"))  # 9
print(name.find("h"))  # -1
print(name.index("s"))  # 10
# print(name.index("h"))  # ValueError: substring not found
print(name.count("e"))  # 2
print(name.startswith("bre"))  # True
print(name.startswith("lin"))  # False
print(name.endswith("se"))  # True
print(name.endswith("lin"))  # False

# Modification and Formatting:
# strip(): Removes leading and trailing whitespace.
# lstrip(): Removes leading whitespace.
# rstrip(): Removes trailing whitespace.
# replace(old, new): Replaces all occurrences of old with new.
# split(delimiter): Splits the string into a list of substrings using the specified delimiter.
# join(iterable): Concatenates strings in an iterable using the string as a separator.
# center(width, fillchar): Returns a centered string of a specified width, padded with fillchar.
# ljust(width, fillchar): Returns a left-justified string.
# rjust(width, fillchar): Returns a right-justified string.

print(" bredlin jose  ".strip())  # bredlin jose  # remove additional space in the 1st and last
print(" bredlin jose  ".lstrip())  # bredlin jose    # remove additional space in the 1st
print(" bredlin jose  ".rstrip())  #  bredlin jose  # remove additional space in the last
print(" bredlin jose  ".replace(" ", "_"))  # bredlin_jose
print(word.split(" "))  # ['my', 'name', 'is', 'Bredlin', 'Jose']
print("_".join(['my', 'name', 'is', 'Bredlin', 'Jose']))  # my_name_is_Bredlin_Jose

# Checking String Content:
# isalnum(): Checks if all characters are alphanumeric.
# isalpha(): Checks if all characters are alphabetic.
# isdigit(): Checks if all characters are digits.
# islower(): Checks if all cased characters are lowercase.
# isupper(): Checks if all cased characters are uppercase.
# isspace(): Checks if all characters are whitespace.

print(word.islower())  # False
print(word.isupper())  # False
print("ac ".isalpha())  # False  # empty space is not considered as alphabets
print("ac4".isalnum())  # True
print("4".isdigit())  # True
print("  ".isspace())  # True
