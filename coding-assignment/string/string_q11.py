# The First Non-repeated Character
from collections import Counter

def first_non_repeated(s):
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example usage
print(first_non_repeated("aabcc"))  # Output: "b"
