from password import generate_password


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
    

def test_password_symbol_character():
    password = generate_password()

    assert contains(password, ['@' '!', '#', '$', '%', '^', '&', '*'])

def test_password_length():
    password = generate_password()

    assert len(password) == 10

def test_password_unique():
    password_one = generate_password
    pasword_two = generate_password
    assert password_one != password_two

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]

from password import generate_password




def test_password_alpha_characters():
   password = generate_password()
   assert password[0].isalpha() and password[1].isalpha() and password[2].isalpha() and password[3].isalpha() and password[4].isalpha()
   # First 5 characters should be lowercase letters




def test_password_numeric_characters():
 password = generate_password()
assert password[5].isdigit() and password[6].isdigit() and password[7].isdigit() and password[8].isdigit()
   # Next 4 characters should be digits




def test_password_symbol_character():
   password = generate_password()
   symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
   assert contains(password[9], symbols)




def test_password_length():
   password = generate_password()
   assert len(password) == 10




def test_password_unique():
   password1 = generate_password()
   password2 = generate_password()
   assert password1 != password2




def contains(s: str, collection: list):
   # check if any characters in collection are present in s
   return any(c in s for c in collection)

