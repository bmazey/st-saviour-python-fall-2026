
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """
    # combines strings c and s using +
    y = c + s
    return y

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """
    #combines strings s and c using +
    #the new string has string s before c
    k = s + c
    return k

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """
    #using[:] the given string prints starting from the index number 1
    ww = s[1:len(s)]
    return ww

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """
    #using [:] the given string prints starting from index number 0
    #using len(s)-1 removes the last character from the string
    ll = s[0:(len(s)-1)]
    return ll
