# mutant_password_module.py
# МУТАНТ: Изменили логику в check_password_strength

import math
import random
import string


def generate_password(length=8, use_digits=True, use_special_chars=False):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")

    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += "!@#$%^&*"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def check_password_strength(password):
    if len(password) < 8:
        return "Слабый"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if score == 4:
        return "Слабый"
    elif score == 3:
        return "Сильный"
    elif score == 2:
        return "Средний"
    else:
        return "Слабый"


def validate_password_rules(password, min_length=8):
    if len(password) < min_length:
        return False, f"Пароль должен быть не менее {min_length} символов"

    if not any(c.isupper() for c in password):
        return False, "Пароль должен содержать заглавные буквы"

    if not any(c.islower() for c in password):
        return False, "Пароль должен содержать строчные буквы"

    return True, "Пароль соответствует требованиям"


def password_entropy(password):
    char_pool = 0
    if any(c.islower() for c in password):
        char_pool += 26
    if any(c.isupper() for c in password):
        char_pool += 26
    if any(c.isdigit() for c in password):
        char_pool += 10
    if any(c in "!@#$%^&*" for c in password):
        char_pool += 8

    if char_pool == 0:
        return 0
    entropy = len(password) * math.log2(char_pool)
    return round(entropy, 2)


def suggest_password_improvement(password):
    suggestions = []

    if len(password) < 12:
        suggestions.append("Увеличьте длину пароля до 12+ символов")

    if not any(c.isdigit() for c in password):
        suggestions.append("Добавьте цифры")

    if not any(c in "!@#$%^&*" for c in password):
        suggestions.append("Добавьте специальные символы")

    return suggestions if suggestions else ["Пароль хороший"]
