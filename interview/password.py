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

    generated_password = ''

    # Generate first 5 characters (lowercase letters)
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(5):
        generated_password += random.choice(lowercase)

    # Generate next 4 characters (digits)
    for i in range(4):
        generated_password += str(random.randint(0, 9))

    # Generate final character (symbol)
    symbols = '!@#$%^&*'
    generated_password += random.choice(symbols)

    return generated_password

# The program uses random numbers to generate each part of the password
