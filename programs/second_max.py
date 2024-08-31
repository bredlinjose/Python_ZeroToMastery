def second_max_using_sort_and_index(nums):
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    nums.sort()  # ascending order
    return nums[-2]

def second_max_by_removing_max(nums):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    nums.remove(max(nums))
    return max(nums)

def second_max_using_sorted_method(nums):
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    return sorted(nums)[-2]

def second_max_using_loop(nums):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    fmax = min(nums)
    smax = 0
    for i in range(len(nums)):
        if nums[i] > fmax:
            smax = fmax
            fmax = nums[i]
        elif nums[i] > smax:
            smax = nums[i]
    return smax


nums = [1, 6, 4, 9, 7, 3, 5, 2]
print(second_max_using_sort_and_index(nums))
nums = [1, 6, 4, 9, 7, 3, 5, 2]
print(second_max_by_removing_max(nums))
nums = [1, 6, 4, 9, 7, 3, 5, 2]
print(second_max_using_sorted_method(nums))
nums = [1, 6, 4, 9, 7, 3, 5, 2]
print(second_max_using_loop(nums))

