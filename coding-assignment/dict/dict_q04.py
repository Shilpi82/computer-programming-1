# key for the maximum value in a dictionary
my_dict = {"a": 1, "b": 3, "c": 2}
max_key = max(my_dict, key=my_dict.get)
print(max_key)  # Output: 'b'
