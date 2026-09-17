
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """

    # TODO

    # use concatenation to add 2 strings
    newstr = c + s
    return newstr
    # return ''

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """

    # TODO
    #use concatenation to add 2 strings

    newstr = s + c
    return newstr
    # return ''

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """

    # TODO

    # use len(x) to find the length, use x[index : index] to create substring
    newstr = s[1 : len(s) - 1]
    return newstr
    # return ''

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """

    # TODO

    # same as shred first, but exclude the last character
    newstr = s[0 : len(s) - 2]
    return newstr
    # return ''
