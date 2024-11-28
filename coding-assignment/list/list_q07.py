#Find the Second Largest Number
def secondLargest(nums: list) -> int:
    first, second = float('-inf'), float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else -1
