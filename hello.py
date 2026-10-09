import random

if __name__ == '__main__':

    s = 'abcdefghijklmnopqrstuvwxyz'

    r = random.randint(0, len(s) - 1)

    print('the random number r is: ' + str(r))

    c = s[r]

    print('the random character is: ' + c)

    