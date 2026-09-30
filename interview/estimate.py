
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # we can see what the decimal is by using modulo!!
    if number % 1 >= 0.5:

    # the program checks the decimal of the number and increades it by 1 if its >= 0.5
        return int(number) + 1
    
    # if it is less than 0.5, the program returns the integer part of the original number
    else: 
        return int(number)
  

