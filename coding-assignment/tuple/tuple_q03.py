#Function that returns the index of an element in a tuple
def find_index(tup, element):
    return tup.index(element) if element in tup else -1

print(find_index((1, 2, 3, 4), 3))  # Output: 2
print(find_index((1, 2, 3, 4), 5))  # Output: -1

