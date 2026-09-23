
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function

    number = number - int(number)
    rounded = int(number)

    if number >= 0.5:
        return rounded + 1
    else:
        return rounded  