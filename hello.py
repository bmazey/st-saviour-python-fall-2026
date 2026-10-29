

if __name__ == '__main__':
    # this is a comment
    print('new dawn, new day!')

def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

    # TODO
    for number in numbers:
        print (number)
    
    return 0

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """

    numbers = [8, 9, 1, -2, 0]
    for number in numbers:
        if number < 0:
            print (number)

    return 0