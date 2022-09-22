from twttr import shorten
import pytest

def test_shorten():
    assert shorten("mama") == "mm"
    assert shorten("hEEELLLLoooooo") == "hLLLL"
    assert shorten("aeiou") == ""
    assert shorten("mijau") == "mj"
    assert shorten("mijau..123") == "mj..123"