#Sort List of Strings by Length
def sortByLength(strs: list) -> list:
    return sorted(strs, key=len)
