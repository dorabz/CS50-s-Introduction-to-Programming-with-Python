from bank import value
import pytest

def test_value():
    assert value('Hello') == 0
    assert value('What’s up!') == 100
    assert value("hwryu") == 20
    assert value("gasdfghjkiu!") == 100
