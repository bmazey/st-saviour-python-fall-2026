

def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """

    staple = c + s
    return staple

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """

    staple = s + c
    return staple

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """

    shred = s[1::1]
    return shred

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_last_character('st. saviourr') -> 'st. saviour'
    """

    shred = s[:-1:1]
    return shred
