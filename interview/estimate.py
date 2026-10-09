
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    decimal = number - int(number)

    if decimal >= 0.5:
        return int(number) + 1
    else: 
        return int(number)

