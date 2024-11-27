#Function to find the common elements between two lists
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

