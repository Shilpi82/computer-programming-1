# Function that checks if a number is prime.
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(10))  # Output: 15
