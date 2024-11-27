#Function that removes duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 5, 5]))  # Output: [1, 2, 3, 4, 5]
