
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    #get the decimal by subtracting the int of the number from the original number
    adot = number - int(number)

    #check if the decimal is > or = to 0.5
    if adot >= 0.5:
        return int(number) + 1
    else:
        return int(number)
