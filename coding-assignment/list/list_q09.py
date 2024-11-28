#Find Missing Numbers in a Range
def findMissing(nums: list, n: int) -> list:
    return list(set(range(1, n + 1)) - set(nums))
