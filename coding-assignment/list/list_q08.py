# Check if List is Sorted
def isSorted(nums: list) -> bool:
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
