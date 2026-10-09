from password import generate_password


def test_password_alpha_characters():
   password = generate_password()
   assert password[0].isalpha() and password[1].isalpha() and password[2].isalpha() and password[3].isalpha() and password[4].isalpha()
   # First 5 characters should be lowercase letters

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
