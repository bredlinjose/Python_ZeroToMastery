def two_sum_using_nested_loop(numbers, target):
    # Time complexity: O(n^2)
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return []

def two_sum_using_dict(numbers, target):
    # Time complexity: O(n)
    dictionary = {}
    n = len(numbers)
    for i in range(n):
        complement = target - numbers[i]
        if complement in dictionary:
            return [dictionary[complement], i]
        dictionary[numbers[i]] = i
        print(dictionary)
    return []


numbers = [1, 4, 2, 4, 3, 9]
target = 8
print(two_sum_using_nested_loop(numbers, target))
print(two_sum_using_dict(numbers, target))
