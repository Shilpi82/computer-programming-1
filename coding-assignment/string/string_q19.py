#Check if a String is a Number
def isNumber(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
