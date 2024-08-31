def reverse_string_using_loop(s):
    # Time complexity: O(n)
    # Space complexity: O(1)
    rev = ""
    for i in s:
        rev = i + rev
    return rev

def reverse_string_using_extended_slice(s):
    # Time complexity: O(n)
    # Space complexity: O(1)
    rev = s[::-1]
    return rev

def reverse_string_using_reversed_method(s):
    # Time complexity: O(n)
    # Space complexity: O(n)
    rev = "".join(reversed(s))
    return rev

def reverse_string_using_function_call(s):
    # Time complexity: O(n)
    # Space complexity: O(1)
    li = list(s)
    li.reverse()
    rev = "".join(li)
    return rev


print(reverse_string_using_loop("my name is bredlin"))
print(reverse_string_using_extended_slice("my name is bredlin"))
print(reverse_string_using_reversed_method("my name is bredlin"))
print(reverse_string_using_function_call("my name is bredlin"))
