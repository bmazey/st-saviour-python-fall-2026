from password import generate_password
import re

def test_password_alpha_characters():
    # TODO BONUS ensure that the first 5 characters are letters
    
    #use regex to check if the first 5 characters are letters
    password1 = generate_password()[0 : 4]
    pattern = r"[a-z]"
    match = re.search(pattern , password1)
    assert match

def test_password_numberic_characters():
    # TODO BONUS ensure the placement of the 4 digit characters

    # use regex to check if the characters from index 5 to 8 are numbers
    password1 = generate_password()[5 : 8]
    pattern = r"[0 - 9]"
    match = re.search(pattern, password1)
    assert match

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol

    # use regex to check that the last character is a symbol
    password1 = generate_password()[9]
    pattern = r"[!@#$%^&*]"
    match = re.search(pattern, password1)
    assert match

def test_password_length():
    # TODO BONUS ensure the length of the password is 10

    # check len(str) == 10
    password1 = generate_password()
    assert len(password1) == 10

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct

    # use password method to create 2 passwords, use != to check if they are unequal
    password1 = generate_password()
    password2 = generate_password()
    assert password1 != password2

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
