# Sort List of Tuples by Second Element
def sortBySecondElement(tuples: list) -> list:
    return sorted(tuples, key=lambda x: x[1])
