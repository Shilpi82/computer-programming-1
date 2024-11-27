# Function that checks whether a number is Armstrong 
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(digit) ** num_digits for digit in num_str)

print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
