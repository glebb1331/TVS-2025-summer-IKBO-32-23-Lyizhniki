import pytest
from password_module import *

def test_generate_password():
    password = generate_password(10)
    assert len(password) == 10
    assert any(c.isalpha() for c in password)
    
    with pytest.raises(ValueError):
        generate_password(3)

def test_check_password_strength():
    assert check_password_strength("short") == "Слабый"
    assert check_password_strength("LongPassword123") == "Сильный"
    assert check_password_strength("Very$tr0ngP@ss!") == "Очень сильный"

def test_validate_password_rules():
    valid, msg = validate_password_rules("Short1")
    assert not valid
    
    valid, msg = validate_password_rules("GoodPassword123")
    assert valid

def test_password_entropy():
    # Этот тест должен выявить намеренную ошибку
    entropy = password_entropy("Test123!")
    # Энтропия должна быть больше, чем просто длина * 2
    assert entropy > 16  # Фактически будет 16, но должно быть больше

def test_suggest_password_improvement():
    suggestions = suggest_password_improvement("short")
    assert "Увеличьте длину" in suggestions[0]