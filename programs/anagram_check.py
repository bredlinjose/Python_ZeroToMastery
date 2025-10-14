def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


if is_anagram(1, "ttsr"):
    print("Anagram")
else:
    print("Not Anagram")
