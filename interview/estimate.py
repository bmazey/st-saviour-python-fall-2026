
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # get the decimal by subtracting the int of number from the original float
    decimal = number - int(number)

    # check if the decimal is greater than or equal to 0.5
    if decimal >= 0.5:
        return int(number) + 1
    else:
        # handle the caser where we round down
        return int(number)
