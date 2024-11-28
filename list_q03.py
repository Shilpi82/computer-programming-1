#Find the Missing Number
def missingNumber(nums: list) -> int:
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)
