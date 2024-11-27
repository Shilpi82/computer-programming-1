# Count the occurrences of items in a dictionary
from collections import Counter
my_dict = {"apple": 3, "banana": 2, "orange": 5}
counter = Counter(my_dict)
print(counter)  # Output: Counter({'orange': 5, 'apple': 3, 'banana': 2})
