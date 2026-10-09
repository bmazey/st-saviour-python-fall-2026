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

    """First to get the 5 random letters create a variable with all of the letters of the alphabet.
    Make strings to randomly choose an index number of the alphabet and add five of them to the final password."""
    
    z = 'abcdefghijklmnopqrstuvwxyz'
    
    a = random.randint(0, 25)
    b = random.randint(0, 25)
    c = random.randint(0, 25)
    d = random.randint(0, 25)
    e = random.randint(0, 25)
    
    f = z[a]
    g = z[b]
    h = z[c]
    i = z[d]
    j = z[e]

    """Do the same thing instead with numbers and add four to the final password."""

    y = '0123456789'

    k = random.randint(0, 9)
    l = random.randint(0, 9)
    m = random.randint(0, 9)
    n = random.randint(0, 9)

    o = y[k]
    p = y[l]
    q = y[m]
    r = y[n]

    """One more time but with symbols and only add one"""

    s = '!@#$%^&*'

    t = random.randint(0, 7)

    u = s[t]

    """Return the password with all of the letters in order with 5 letters, 4 numbers, and one symbol."""

    return f+g+h+i+j+o+p+q+r+u