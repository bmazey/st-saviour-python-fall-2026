
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    if number % 1 >= 0.5:
        return int(number) + 1
    else: 
        return int(number)
# The program uses modulo operator to check the decimal portion of the number
