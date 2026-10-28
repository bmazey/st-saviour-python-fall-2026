
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

    sum = 0

    for number in numbers:
        sum += number
    # this loop takes each number in the list and adds it to the sum variable, which starts at 0. after the loop completes, the function returns the total sum of the numbers in the list.

    return sum

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """

    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            return i
        i += 1
    # this loop iterates through the list of numbers and checks each number to see if it is negative. if a negative number is found, the function returns its position in the list. if no negative number is found after checking all the numbers, the function returns -1 to indicate that no negative number was found.

    return -1

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """

    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    # this loop checks a list of numbers to find which one is the greatest, then returns that number.

    return greatest

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """

    banished = []
    for number in numbers:
        if number != n:
            banished.append(number)
    # this loop goes through the list of numbers and checks each number to see if it is equal to n. if a number is not equal to n, it is added to the banished list. after checking all the numbers, the function returns the new list banished, which contains all the numbers from the original list except for those who are banished.

    return banished

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """

    rounded = []
    for f in floats:
        if f - int(f) >= 0.5:
            rounded.append(int(f) + 1)
        else:
            rounded.append(int(f))
    # this loop checks a list of floats for their decimal value. it then returns the next integer if it is 0.5 or greater and the integer outside of the decimal if it is 0.4 or less.

    return rounded

def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """

    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    # this loop checks a list to see if all the numbers are even by using modulo. it puts these nubers in a list and skips a number if it is odd

    return evens

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    last = []
    for number in numbers:
        last.append(number % 10)
    # this loop checks a list to find the last digit of each 4 digit number by using modulo and returns that value
    return last

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

    merge = first + second
    merge.sort()
    # this function checks every number's value in a list and returns them all as a new list

    return merge