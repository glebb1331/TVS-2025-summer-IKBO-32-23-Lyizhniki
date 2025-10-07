def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Рост должен быть больше нуля.")
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Недостаток веса"
    elif 18.5 <= bmi < 25:
        return "Норма"
    elif 25 <= bmi < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"


def healthy_weight_range(height):
    min_w = 18.5 * (height ** 2)
    max_w = 24.9 * (height ** 2)
    return round(min_w, 1), round(max_w, 1)


def is_healthy_bmi(bmi):
    return 18.5 <= bmi <= 24.9


def bmi_advice(bmi):
    if bmi > 18.5:  # МУТАЦИЯ!
        return "Слишком низкий вес"
    elif bmi > 24.9:
        return "Слишком высокий вес"
    else:
        return "Нормальный вес"
