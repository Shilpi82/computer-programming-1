#Find Pairs in List with Given Difference
def findPairs(nums: list, diff: int) -> list:
    nums_set = set(nums)
    pairs = []
    for num in nums:
        if num + diff in nums_set:
            pairs.append((num, num + diff))
    return pairs
