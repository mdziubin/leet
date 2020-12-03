def twosum(nums, target):
    d = {}
    for i, val in enumerate(nums):
        m = target - val
        if m in d:
            return [d[m], i]
        else:
            d[val] = i


nums = [10, 20, 4, 5, 6]
target = 26
print(twosum(nums, target))
