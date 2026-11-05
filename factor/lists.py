
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

    # TODO

    # save the sum in a separate variable
    sum = 0
    # use enhanced for loop to go over the list, and add each number to sum
    for number in numbers:
        sum += number
    return sum

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """

    # TODO

    # use a while loop to check if the number we're currently on is negative
    i = 0
    while i < len(numbers):
        if(numbers[i] < 0):
            return i
        i += 1
    return 0

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """

    # TODO

    # save the current greatest number here
    greatest = 0

    # check if the number we're currently on is greater than the current greatest number
    i = 0
    while i < len(numbers):
        if(numbers[i] > greatest):
            greatest = numbers[i]
        i += 1
    return greatest

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """

    # TODO

    # loop over the list an undetermined amount of times, removing any instances of n until there is no more n in the list
    while numbers.count(n) >= 1:
        numbers.remove(n)

    return numbers

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """

    # TODO

    # loop over the list, check if the decimal component is greater or less than than 0.5
    # returns the whole number component if less than, returns the whole number component + 1 if greater than
    return [int(x) if x % 1 < 0.5 else int(x) + 1 for x in floats]

def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """

    # TODO

    # pro gamer technique: use a list comprehension to loop over the list, check if they're even, and return those numbers
    return [x for x in numbers if x % 2 == 0]

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    # TODO

    # pro gamer technique: use a list comprehension to loop over the list and keep only the last digit from each element
    return [x % 10 for x in numbers]

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

    # TODO +5 Bonus

    # add the second list to the first, then sort the list
    first.append(second)
    return first.sort()