
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function

    """Get decimal value by subtracting the in of number from the original"""

    num = number - int(number)

    """Check if the decimal is greater than or equal o 0.5"""
    if num >= 0.5:
        return int(number) + 1
    else:
        return int(number)  
    