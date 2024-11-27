# Flatten a dictionary of dictionaries into a single dictionary
nested_dict = {"a": {"x": 1}, "b": {"y": 2}, "c": {"z": 3}}
flat_dict = {f"{key}_{subkey}": subvalue for key, subdict in nested_dict.items() for subkey, subvalue in subdict.items()}
print(flat_dict)  # Output: {'a_x': 1, 'b_y': 2, 'c_z': 3}

