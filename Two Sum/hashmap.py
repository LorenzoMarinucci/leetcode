def twoSum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        comp = target - num
        if (comp in dict):
            return [dict[comp], i]
        else:
            dict[num] = i