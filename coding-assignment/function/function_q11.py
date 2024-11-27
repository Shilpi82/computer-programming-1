#Function that returns the second largest number in a list
def second_largest(nums):
    nums = list(set(nums))  # Remove duplicates
    nums.sort()
    return nums[-2] if len(nums) > 1 else None

print(second_largest([4, 3, 2, 1]))  # Output: 3
