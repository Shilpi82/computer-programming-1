#Function that checks if a number is positive, negative, or zero
def check_sign(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    return "Zero"

print(check_sign(5))    # Output: Positive
print(check_sign(-3))   # Output: Negative
print(check_sign(0))    # Output: Zero
