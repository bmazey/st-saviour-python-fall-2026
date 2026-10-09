
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """

    # TODO
    """Adding two strings c and s together to return them combined in the correct order."""
    x = c + s
    return x

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """

    # TODO
    """Adding two strings s and c together to return them combined."""
    y = s + c
    return y

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """

    # TODO
    """To remove the first letter from the string s, start the string at index number 1 and continue the rest of its length"""
    z = s[1 : len(s)]
    return z

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """

    # TODO
    """To remove the last letter from the string s, start the string at index number 0 and minus one from its length to shred the last letter"""
    a = s[0 : len(s) - 1]
    return a
