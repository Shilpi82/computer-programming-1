# Create a dictionary with a specific value for each key in a list of keys
keys = ["a", "b", "c"]
value = 0
my_dict = {key: value for key in keys}
print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# Using fromkeys
my_dict = dict.fromkeys(keys, value)
print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
