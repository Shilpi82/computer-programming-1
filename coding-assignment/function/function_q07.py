# Function to calculate the power of a number without using the ** operator
def power(base, exp):
    result = 1
    for _ in range(abs(exp)):
        result *= base
    if exp < 0:
        return 1 / result
    return result

print(power(2, 3))  # Output: 8
print(power(2, -2))  # Output: 0.25
