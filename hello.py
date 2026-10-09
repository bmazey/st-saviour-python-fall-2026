

if __name__ == '__main__':
    # this is a comment
    print('new dawn, new day!')

    # homework = False
    # due_next_period = True

    # if homework and due_next_period:
    #     print('Homework is due next period, locking in.')

    # elif homework:
    #     print('Homework is due tomorrow, I\'ll do it during fifth period.')

    # else:
    #     print('No homework tonight -- I can relax.')
    # y = 5.8
    # x = int(y)
    # print('x is ' + str(x) + ' the type of x is ' + str(type(x)))

    #x = 5.8
    #print(x % 1)

    #EX: from interview password import generate_password
    #then write: print(generate_password()) *indented

    #+= means adding on to the end of the string
    import random

    #def generate_password() -> str:

    #s = 'october'

    #r = random.randint(0, 6)

    #print ('the number is: ' + str(r))
    
    #c = s[r]

    #print('the random character is: ' + c)"""

    #l : str['abcdefghijklmnopqrstuvwxyz']
    #e = random.randint(0, 25)

    #d = '0123456789'
    #print(d[::])
    #i = random.randit(0, 9)

    #syb = '!@#$%&()?'
    #mol = random.randit(0, 8)

    #print(str(e) + str(i) + str(mol))
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
    
    d = '0123456789'
    i = random.randint(0, 9)
    i2 = random.randint(0, 9)
    i3 = random.randint(0, 9)
    i4 = random.randint(0, 9)
    g = d[i]
    h = d[i2]
    j = d[i3]
    k = d[i4]
    
    syb = '!@#$%&()?'
    mol = random.randint(0, 8)
    r = syb[mol]
    
    fp = print(t + v + w + x + y + g + h + j + k + r)
    sp = print(r + k + j + h + g + y + x + w + v + t)
