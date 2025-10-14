def bubble_sorting(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


numbers = [3, 5, 9, 1, 4, 8, 2, 7]
sorted_num = bubble_sorting(numbers)
print(sorted_num)