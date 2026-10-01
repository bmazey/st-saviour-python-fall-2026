
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

 # using modulo to figure out if a number is a multiple of 7 and 11
 # it has to be first, because it needs to check that this statement is true/false before anything else
    if number % 7 == 0 and number % 11 == 0:
        return('seveneleven')

    # determine if the number is a multiple of 7 using %
    elif number % 7 == 0:
        return('seven')

    # determine if the number is a multiple of 11 using %
    elif number % 11 == 0:
        return('eleven')  
    
    # if the number is not a multiple of either, it will return an empty string
    return ''
