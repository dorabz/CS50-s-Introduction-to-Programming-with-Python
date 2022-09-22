import pytest
from um import count

def test_convert():
    assert count("um") == 1
    assert count("podrum") == 0
    assert count("UM") == 1
    assert count("umumumum") == 0