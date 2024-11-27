# Remove duplicates from a dictionary (i.e., keeping only unique values)?
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
unique_values_dict = {key: value for key, value in my_dict.items() if value not in list(my_dict.values())}
print(unique_values_dict)  # Output: {'b': 2, 'd': 3}
