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

    # use random.randint to generate a random index number
    # the random index number will be used to generate a random letter
    l = 'abcdefghijklmnopqrstuvwxyz'
    e = random.randint(0, 25)
    e2 = random.randint(0, 25)
    e3 = random.randint(0, 25)
    e4 = random.randint(0, 25)
    e5 = random.randint(0, 25)
    t = l[e]
    v = l[e2]
    w = l[e3]
    x = l[e4]
    y = l[e5]

    # use random.randint to generate a random index number
    # the random index number will be used to generate a random number
    d = '0123456789'
    i = random.randint(0, 9)
    i2 = random.randint(0, 9)
    i3 = random.randint(0, 9)
    i4 = random.randint(0, 9)
    g = d[i]
    h = d[i2]
    j = d[i3]
    k = d[i4]

    # use random.randint to generate a random index number
    # the random index number will be used to generate a random symbol
    syb = '!@#$%&()?'
    mol = random.randint(0, 8)
    r = syb[mol]

    # this will generate the 10 character password
    fp = print(t + v + w + x + y + g + h + j + k + r)
    sp = print(r + k + j + h + g + y + x + w + v + t)
    
