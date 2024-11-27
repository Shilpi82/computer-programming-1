# Function that takes a list of numbers and returns the sum of all even numbers
def sum_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)

print(sum_even([1, 2, 3, 4, 5]))  # Output: 6
