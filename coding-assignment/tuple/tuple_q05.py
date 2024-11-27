#Function that counts the number of occurrences of an element in a tuple
def count_occurrences(tup, element):
    return tup.count(element)

print(count_occurrences((1, 2, 2, 3), 2))  # Output: 2
