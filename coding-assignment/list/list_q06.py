#All Pairs That Sum to a Target
def twoSum(nums: list, target: int) -> list:
    seen = {}
    result = []
    for num in nums:
        complement = target - num
        if complement in seen:
            result.append([complement, num])
        seen[num] = True
    return result
