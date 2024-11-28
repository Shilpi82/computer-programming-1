#Move Negative Numbers to Front
def moveNegativesToFront(nums: list) -> None:
    negative_nums = [num for num in nums if num < 0]
    non_negative_nums = [num for num in nums if num >= 0]
    nums[:] = negative_nums + non_negative_nums
