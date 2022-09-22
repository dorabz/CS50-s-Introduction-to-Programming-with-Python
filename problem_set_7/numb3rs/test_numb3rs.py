from numb3rs import validate

def test_validate():
    assert validate("pizza") == False
    assert validate("10.220.9.8") == True
    assert validate("555555.255.255.255") == False
    assert validate("654.765.8.0") == False
    assert validate("63.321.52.9") == False

