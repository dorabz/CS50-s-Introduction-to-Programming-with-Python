from plates import is_valid
import pytest

def test_is_valid():
    assert is_valid("O!M65") == False
    assert is_valid("SDTYUIOIHGVBJKL") == False
    assert is_valid("ABA34A") == False
    assert is_valid("BU30") == True
    assert is_valid("B") == False
    assert is_valid("MN03") == False
    assert is_valid("98YYY") == False
    assert is_valid("11") == False
    assert is_valid("WE5.23") == False



