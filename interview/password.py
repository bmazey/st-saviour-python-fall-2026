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

    y = '0123456789'

    k = random.randint(0, 9)
    l = random.randint(0, 9)
    m = random.randint(0, 9)
    n = random.randint(0, 9)

    o = y[k]
    p = y[l]
    q = y[m]
    r = y[n]

    s = '!@#$%^&*'

    t = random.randint(0, 7)

    u = s[t]


    return f+g+h+i+j+o+p+q+r+u