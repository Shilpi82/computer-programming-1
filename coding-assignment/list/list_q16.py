#Find the First Missing Positive Integer
def firstMissingPositive(nums: list) -> int:
    nums = set(nums)
    i = 1
    while i in nums:
        i += 1
    return i
