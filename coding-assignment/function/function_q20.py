#Function to find the most frequent element in a list
def most_frequent(lst):
    from collections import Counter
    freq = Counter(lst)
    return freq.most_common(1)[0][0]

print(most_frequent([1, 2, 3, 2, 3, 2]))  # Output: 2
