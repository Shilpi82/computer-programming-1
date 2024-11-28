#Remove All Punctuation from String
import string

def remove_punctuation(s):
    return ''.join(char for char in s if char not in string.punctuation)

# Example usage
print(remove_punctuation("Hello, world!"))  # Output: "Hello world"
