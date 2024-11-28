#Check if a String is a Rotation of Another
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s1 in (s2 + s2)

# Example usage
print(is_rotation("abc", "cab"))  # Output: True
