from password import generate_password


def test_password_alpha_characters():
    # TODO BONUS ensure that the first 5 characters are letters
    #use regex to check if the first 5 are letters
    # assert!!!
    pass

def test_password_numberic_characters():
    # TODO BONUS ensure the placement of the 4 digit characters
    # use regex to check if the 4 are numbers
    pass

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol
    # regex!!!
    pass

def test_password_length():
    # TODO BONUS ensure the length of the password is 10
    # check len(str) == 10
    pass

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct
    # use password method to create 2 passwords, use == to check if they are equal
    pass

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
