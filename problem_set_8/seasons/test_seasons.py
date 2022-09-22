from seasons import textualize
import pytest

def test_textualize():
    assert textualize("12477600") == "twelve million, four hundred seventy-seven thousand, six hundred"


