from password import generate_password


import string
import re

def test_password_alpha_characters():
    password = generate_password()

    assert password[0].isalpha()
    assert password[1].isalpha()
    assert password[2].isalpha()
    assert password[3].isalpha()
    assert password[4].isalpha()

def test_password_numberic_characters():
    password = generate_password()

    assert password[5].isdigit()
    assert password[6].isdigit()
    assert password[7].isdigit()
    assert password[8].isdigit()

def test_password_symbol_character() :
    password = generate_password()
    assert contains(password, ['@', '!', '#', '$', '%', '^', '&', '*'])

def test_password_length():
    password = generate_password()
    assert len(password) == 10

def test_password_unique():
    password_one = generate_password()
    password_two = generate_password()
    assert password_one != password_two

def contains(s: str, collection: list):
    return any(c in s for c in collection)

