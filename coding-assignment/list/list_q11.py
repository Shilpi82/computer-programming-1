# Find Pairs With Sum Less Than Target
def countPairs(nums: list, target: int) -> int:
    nums.sort()
    left, right, count = 0, len(nums) - 1, 0
    while left < right:
        if nums[left] + nums[right] < target:
            count += (right - left)
            left += 1
        else:
           
