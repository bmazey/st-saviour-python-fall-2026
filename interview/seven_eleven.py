
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # TODO implement seven_eleven function

    # checks if the number is divisible by 7 and/or 11
     
    if number % 7 == 0 and number % 11 == 0:
            return "seveneleven"
    elif number % 7 == 0:
        return "seven"
    elif number % 11 == 0:
        return "eleven"
    else:
        return ''

    # return ''
