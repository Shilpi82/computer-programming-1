#Remove Duplicates from String
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# Example usage
print(remove_duplicates("aabbccdd"))  # Output: "abcd"
