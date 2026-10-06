
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function
    # get the decimal by subtracting the int of number from the original 
    decimal = number - int(number) + 1
    # check if the number is greater than or equal to 0.5
    remainder = number % 1 
    if remainder >= 0.5: 
        return int(number) +1
    else:
        return int(number)
    

    
