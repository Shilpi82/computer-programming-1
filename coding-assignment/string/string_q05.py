#Replaces all spaces in a string with %20
def replace_spaces(s):
    return s.replace(" ", "%20")

print(replace_spaces("Hello World"))  # Output: "Hello%20World"
