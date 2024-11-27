# Find the unique keys across two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
unique_keys = set(dict1.keys()) ^ set(dict2.keys())
print(unique_keys)  # Output: {'a', 'c'}
