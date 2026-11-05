
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """
    # this goes through all the numbers and sums them together 
    sum = 0
    i = 0 
    while i < len(numbers):
        sum += numbers[i]
        i += 1 

    # gives the sum
    return sum 

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """
    i = 0
    # this loop iterates the list of numbers and checks each number to see if its negative 
    while i < len(numbers): 
        if numbers [i] < 0:
            return i 
        i += 1 


    return 0

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """
    greatest = numbers[0]

    # this loop checks a list of numbers to find which one is the greatest then returns the greatest one in the list 
    for number in numbers:
        if number > greatest:
            greatest = number                    
    

    return greatest 

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """

    gone = []
    for number in numbers:
        if number != n:
            gone.append(number)
   # this loops just checks the list and checks to see if each number is equal to n 

    return gone
  
def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """
# this loops checks a list of floats for their decimal value 
    rounded = []
    for f in floats:
        decimal = f - int(f)
        if decimal >= 0.5:
            rounded.append(int(f)+ 1)
        else:
            rounded.append(int(f))
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
    return evens 
# this loops checks a list of numbers to see if each number is even by using module it skips the numbers 
   

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """
# this loop checks a list to find the last digit of each 4 digit number by using modulo and returns that value 
    last = []
    for number in numbers: 
        last.append(number % 10)


    return last

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """
    # this function checks the numbers value in the list and returns them all as a new list 
    merge = first + second
    merge.sort()

    return merge 