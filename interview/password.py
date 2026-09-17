import random

def generate_password() -> str:
    """
    generate_password() takes no arguments and produces a string
    which meets the following password complexity requirements:
        - the length of the password is 10
        - the first 5 characters are lower case letters
        - the next 4 characters are digits [0-9]
        - the final character is a symbol [!@#$%^&*]
        - it's relatively uncommon to generate the same password twice 
    """

    # HINT you will require the use of a random number generator for this function
    # https://docs.python.org/3/library/random.html#random.randint

    # TODO implement generate_password function

    # create string that saves the alphabet, and one that will hold the random letters for the password
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = ""

    # loop 5 times to get 5 random letters, saved to variable "letters"
    i = 1
    while i <= 5:
        randletter = alphabet[random.randint(0 , 25)]
        letters = letters + randletter
        i += 1

    # loop 4 times to get 4 random numbers, saved to variable "number"
    number = 0
    j = 1
    while j <= 4 :  
        number = number * 10 + random.randint(0 , 9)
        # every time it's multiiplied ny 10, a new digit at the end is made, and this digit = the random number
        j += 1

    # saves all availible ending special characers, which are then randomly picked and saved into randchar
    char = "!@#$%^&*"
    randchar = char[random.randint(0 , len(char) - 1)]

    return f"{letters}{number}{randchar}"


    # return ''
