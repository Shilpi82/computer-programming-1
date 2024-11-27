# Create a dictionary with default values 
from collections import defaultdict
my_dict = defaultdict(int)
my_dict["age"] += 1
print(my_dict["age"])  # Output: 1
