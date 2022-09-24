from project import get_answer, get_word, check_letter

def test_get_answer():
    assert get_answer("yes") == True
    assert get_answer("nO") == False

def test_get_word():
    assert get_word(0) == "DIALECT"
    assert get_word(9) == "STRANGER"

def test_check_letter():
    assert check_letter("DIALECT", "L", ['_', '_', '_', '_', '_', '_', '_']) == ['_', '_', '_', 'L', '_', '_', '_']
    assert check_letter("DIALECT", "D", ['_', '_', '_', 'L', '_', '_', '_']) == ['D', '_', '_', 'L', '_', '_', '_']




