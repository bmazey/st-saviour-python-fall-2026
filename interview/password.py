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
    password = ''

    s = 'abcdefghijklmnopqrstuvwxyz'

    # add the first letter
    r = random.randint(0, 25) 
    password += s[r]

    # add the second letter
    r = random.randint(0, 25)
    password += s[r] 

    # add the third letter
    r = random.randint(0, 25)
    password += s[r] 

    # add the fourth letter
    r = random.randint(0, 25)
    password += s[r] 

    # add the fifth letter
    r = random.randint(0, 25)
    password += s[r] 

    s = '0123456789'

    # add first digit
    r = random.randint(0, 9) 
    password += s[r] 

   # add second digit
    r = random.randint(0, 9) 
    password += s[r] 

    # add thrid digit
    r = random.randint(0, 9) 
    password += s[r] 

    # add fourth digit
    r = random.randint(0, 9) 
    password += s[r] 

    s = '!@#$%^&*'

    r = random.randint(0, 7)
    password += s[r]

    return password
