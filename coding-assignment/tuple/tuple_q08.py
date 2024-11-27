#Function that checks if a tuple is empty
def is_empty(tup):
    return len(tup) == 0

print(is_empty((1, 2, 3)))  # Output: False
print(is_empty(()))         # Output: True
