#Function that accepts a string and returns the string with vowels removed
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

print(remove_vowels("hello"))  # Output: "hll"
