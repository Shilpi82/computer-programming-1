# remove all keys from a dictionary whose values are equal to a specific value

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
value_to_remove = 1
my_dict = {key: value for key, value in my_dict.items() if value != value_to_remove}
print(my_dict)  # Output: {'b': 2, 'd': 3}
