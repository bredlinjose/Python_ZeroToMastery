def two_sum(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def two_sum_using_dict(nums, target):
    n = len(nums)
    dic = {}
    for i in range(n):
        complement = target - nums[i]
        if complement in dic:
            return [dic[complement], i]
        dic[nums[i]] = i
    return None


nums = [2, 6, 8, 4, 3, 5, 7]
target = 15
# print(two_sum(nums, target))
print(two_sum_using_dict(nums, target))

