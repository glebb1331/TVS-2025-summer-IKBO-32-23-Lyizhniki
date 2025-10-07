import pytest
from bmi_module import calculate_bmi, bmi_category, healthy_weight_range, is_healthy_bmi, bmi_advice


def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 1) == 22.9
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_bmi_category():
    assert bmi_category(17) == "Недостаток веса"
    assert bmi_category(22) == "Норма"
    assert bmi_category(28) == "Избыточный вес"
    assert bmi_category(33) == "Ожирение"


def test_healthy_weight_range():
    min_w, max_w = healthy_weight_range(1.80)
    assert 59.9 <= min_w <= 60.0
    assert 80.5 <= max_w <= 81.0


def test_is_healthy_bmi():
    assert is_healthy_bmi(22.5)
    assert not is_healthy_bmi(30)


def test_bmi_advice():
    assert bmi_advice(17) == "Слишком низкий вес"
    assert bmi_advice(26) == "Слишком высокий вес"
    assert bmi_advice(22) == "Нормальный вес"


def test_bmi_advice_comprehensive():
    assert bmi_advice(18.4) == "Слишком низкий вес"
    assert bmi_advice(18.5) == "Нормальный вес"
    assert bmi_advice(24.9) == "Нормальный вес"
    assert bmi_advice(25.0) == "Слишком высокий вес"

    assert bmi_advice(10) == "Слишком низкий вес"
    assert bmi_advice(40) == "Слишком высокий вес"
