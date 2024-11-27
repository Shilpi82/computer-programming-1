#Function that accepts a number and returns a list of its divisors
def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(divisors(10))  # Output: [1, 2, 5, 10]
