
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """
    # create an empty result string
    result = ''

    # test if the number has a factor of 7 using modulo
    if number % 7 == 0:
        result += 'seven'

    # test if the number has a factor of 11 using modulo
    if number % 11 == 0:
        result += 'eleven'

    # return the result string
    return result
