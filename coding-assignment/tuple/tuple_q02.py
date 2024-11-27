#Function that checks if an element exists in a tuple
def element_exists(tup, element):
    return element in tup

print(element_exists((1, 2, 3, 4), 3))  # Output: True
print(element_exists((1, 2, 3, 4), 5))  # Output: False
