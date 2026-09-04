from estimate import rounder

def test_rounder():
    # ensure that any floating decimal >= .5 gets rounded up
    assert rounder(0) == 0
    assert rounder(.5) == 1

    assert rounder(1.0) == 1
    assert rounder(1.2) == 1

    assert rounder(7.6) == 8
    assert rounder(7.9) == 8