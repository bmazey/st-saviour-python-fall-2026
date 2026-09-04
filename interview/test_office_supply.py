from office_supply import staple_to_front, staple_to_end, shred_first_character, shred_last_character

def test_stapler():
    # verify stapler cases
    assert staple_to_front('anda', 'p') == 'panda'
    assert staple_to_front('aviour', 's') == 'saviour'

    assert staple_to_end('pand', 'a') == 'panda'
    assert staple_to_end('saviou', 'r') == 'saviour'

def test_shredder():
    # verify shredder cases
    assert shred_first_character('ppanda') == 'panda'
    assert shred_first_character('ssaviour') == 'saviour'

    assert shred_last_character('pandax') == 'panda'
    assert shred_last_character('saviourx') == 'saviour'
