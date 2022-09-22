from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(55) == "55%"

def test_convert():
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/5") == 20
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("bla/bla")



