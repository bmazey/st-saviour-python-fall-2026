import random

if __name__ == '__main__':
    # this is a comment
    print('new dawn, new day!')

    number = 0
    j = 1
    while j <= 4 :  
        number = number * 10 + random.randint(0 , 9)
        print(str(number))
        print("the length is: " + str(len(str(number))))
        # every time it's multiiplied ny 10, a new digit at the end is made, and this digit = the random number
        j += 1
