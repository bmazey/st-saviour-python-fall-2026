
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function

   # save the whole number part of the decimal and the decimal part in different variables 
    newnum = number - int(number)
    rounded = int(number)

    # case for positive numbers
    if number >= 0:
        if newnum >= 0.5:
            return rounded + 1
        else:
            return  rounded

    # case for negatives
    if number < 0:

        if newnum <= -0.5:

            return rounded - 1
        else:
            return rounded


    # return 0
