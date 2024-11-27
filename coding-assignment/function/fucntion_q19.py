#Function that checks if a given year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2020))  # Output: True
print(is_leap_year(2023))  # Output: False
