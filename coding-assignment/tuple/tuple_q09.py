#Function that swaps the first and last elements of a tuple.
def swap_first_last(tup):
    if len(tup) < 2:
        return tup
    return (tup[-1],) + tup[1:-1] + (tup[0],)

print(swap_first_last((1, 2, 3, 4)))  # Output: (4, 2, 3, 1)
