
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

    # sum starts at 0 then as it loops it keeps adding the numbers in the list until it adds all
    sum = 0
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

    # goes through list position by position until number is < 0 returns position of number
    i = 0
    while i < len(numbers):
        if(numbers[i] < 0):
            return i
        i += 1

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """

    # goes through list accepts number as greatest until a greater one is found returns greatest number
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

    # counts the amount of n in list then takes away all instances of n until it is gone then returns list without n
    while numbers.count(n) >= 1:
        numbers.remove(n)
    return numbers


def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """

    # goes through list uses % to remove ones if >= 0.5 adds 1 to int of float if < 0.5 returns int of float
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

    # manipulates integers in list by using modulo to only return evens
    return [x for x in numbers if x % 2 == 0]
    

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    # for every loop uses modulo to remove tens from number to get last digit adds it to the empty list
    result = []
    for number in numbers:
        result.append(number % 10)
    return result

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

    # TODO +5 Bonus
    # takes second list and adds it to first then returns sorted merged list
    first.append(second)
    return first.sort()
