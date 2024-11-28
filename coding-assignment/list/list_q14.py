# Find the Kth Largest Element
import heapq

def findKthLargest(nums: list, k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
