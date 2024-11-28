# Rotate List
def rotate(nums: list, k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
