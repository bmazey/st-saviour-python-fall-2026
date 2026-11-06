
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

    # TODO
    # taking the sum and adding it to each number in numbers with +=
    
    sum = 0
    for number in list[int]:
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
    # going through the list of numbers while i is less than its length, and returning the index of the number if it is less than 0
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
    # the loop is going through each number and if the current number is greater the previous one, the greater one is returned
    greatest = 0
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
    # when the number is n, it removes every n from the list
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
    # the while loop goes through every number and when % by 1, if the number is greater than or equal to 0.5, the number is rounded up by 1 with + 1
    # if it is less than 0.5, it will be returned by itself, with no decimal
    i = 0
    while i < len(floats):
        if floats[i] % 1 >= 0.5:
            floats[i] = int(floats [i]) + 1
        else:
            floats[i] = int(floats [i])
        i += 1
    return floats

def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """

    # TODO
    # if the number % by 2 is equal to 0, the number is even and it is returned
    return [x for x in numbers if x % 2 == 0]


def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    # TODO
    # when a number is % 10, all the thousand, hundreds, and tens places are removed and the last digit is left over and returned
    return [x % 10 for x in numbers]

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

    # TODO +5 Bonus
    # adds the second list to the first one and then sorts it
    first.append(second)
    return first.sort()