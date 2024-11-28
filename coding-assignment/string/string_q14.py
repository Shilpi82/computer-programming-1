#Check if Two Strings are Isomorphic
def is_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    mapping = {}
    for char1, char2 in zip(s1, s2):
        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            mapping[char1] = char2
    return True

# Example usage
print(is_isomorphic("egg", "add"))  # Output: True
