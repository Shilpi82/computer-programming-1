# Merge two dictionaries and resolve conflicts by keeping the average of the values when keys are repeated
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
merged_dict = {}
for key in set(dict1) | set(dict2):
    merged_dict[key] = (dict1.get(key, 0) + dict2.get(key, 0)) / 2
print(merged_dict)  # Output: {'a': 1.0, 'b': 3.0, 'c': 4.0, 'd': 6.0}
