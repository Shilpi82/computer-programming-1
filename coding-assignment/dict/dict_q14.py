# Group values of a dictionary by their key length
from collections import defaultdict
my_dict = {"apple": 1, "banana": 2, "pear": 3, "cherry": 4}
grouped = defaultdict(list)
for key, value in my_dict.items():
    grouped[len(key)].append(value)
print(grouped)  # Output: defaultdict(<class 'list'>, {5: [1, 3], 6: [2], 7: [4]})
