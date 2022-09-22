import pytest
from working import convert

def test_convert():
    with pytest.raises(ValueError):
        convert("7AM - 7PM")
    assert convert("6 AM to 12 PM") == "06:00 to 12:00"
    with pytest.raises(ValueError):
        convert("08:00 to 13:00")
    assert convert("10:00 AM to 8:00 PM") == "10:00 to 20:00"
    assert convert("11 PM to 3 AM") == "23:00 to 03:00"

