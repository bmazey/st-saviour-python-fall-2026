import random

if __name__ == '__main__':
    
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

