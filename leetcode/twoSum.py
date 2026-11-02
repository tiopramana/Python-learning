def twoSum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        diff = value - index
        if diff in seen:
            return (seen[diff], index)
        else:
            seen[value] = index
    return