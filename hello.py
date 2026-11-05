

if __name__ == '__main__':
    # this is a comment
    print('new dawn, new day!')

    numbers = [0, 1, 1, 0, 0, 1]
    for number in numbers:
        if number == 0:
            numbers.remove(number)

    print(numbers)