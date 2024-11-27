# Get the most frequent value in a dictionary
from collections import Counter
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}
value_counts = Counter(my_dict.values())
most_common_value = value_counts.most_common(1)[0][0]
print(most_common_value)  # Output: 1
