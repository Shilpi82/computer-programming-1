#Function that checks if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
