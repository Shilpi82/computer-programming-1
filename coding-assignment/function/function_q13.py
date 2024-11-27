#Function that takes a list and returns the number of occurrences of each element
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict

print(count_occurrences([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}
