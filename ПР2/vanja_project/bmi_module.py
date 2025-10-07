def calculate_bmi(weight, height):
    """Рассчитывает индекс массы тела (BMI)."""
    if height <= 0:
        raise ValueError("Рост должен быть больше нуля.")
    return weight / (height ** 2)

def bmi_category(bmi):
    """Определяет категорию по значению BMI."""
    if bmi < 18.5:
        return "Недостаток веса"
    elif 18.5 <= bmi < 25:
        return "Норма"
    elif 25 <= bmi < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"

def healthy_weight_range(height):
    """Возвращает диапазон здорового веса для данного роста."""
    min_w = 18.5 * (height ** 2)
    max_w = 24.9 * (height ** 2)
    return round(min_w, 1), round(max_w, 1)

def is_healthy_bmi(bmi):
    """Проверяет, находится ли BMI в пределах нормы."""
    return 18.5 <= bmi <= 24.9

# def bmi_advice(bmi):
#     """Функция с намеренной ошибкой (логическая ошибка)."""
#     if bmi < 18.5:
#         return "Слишком высокий вес"  #намеренная ошибка
#     elif bmi > 24.9:
#         return "Слишком низкий вес"   #намеренная ошибка
#     else:
#         return "Нормальный вес"

def bmi_advice(bmi):
    """Исправленная функция"""
    if bmi < 18.5:
        return "Слишком низкий вес"  # ИСПРАВЛЕНО
    elif bmi > 24.9:
        return "Слишком высокий вес"   # ИСПРАВЛЕНО
    else:
        return "Нормальный вес"
