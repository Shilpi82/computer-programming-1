#String Rotation
def is_rotation_v2(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

# Example usage
print(is_rotation_v2("abc", "cab"))  # Output: True
