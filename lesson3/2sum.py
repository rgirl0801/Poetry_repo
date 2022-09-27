def two_sum(nums, target):
    res = []
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            res.append([target - nums[i], nums[i]])
        dic[nums[i]] = i
    return res


print(two_sum([2, 7, 11, 15, 1, 8], 9)) # [2, 7]
print(two_sum([3, 2, 2, 4], 6)) # [2, 4]