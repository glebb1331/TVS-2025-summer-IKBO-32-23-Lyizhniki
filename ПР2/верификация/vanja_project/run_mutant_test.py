import sys
import os
sys.path.append(os.path.dirname(__file__))

try:
    from mutant_bmi_module import bmi_advice

    print("ЗАПУСК МУТАЦИОННОГО ТЕСТИРОВАНИЯ")
    print("=" * 50)

    # Тестируем мутанта
    print("1. Тестируем BMI=17 (низкий вес):")
    result1 = bmi_advice(17)
    print(f"   Результат: '{result1}'")
    print(f"   Ожидалось: 'Слишком низкий вес'")

    print("\n2. Тестируем BMI=22 (норма):")
    result2 = bmi_advice(22)
    print(f"   Результат: '{result2}'")
    print(f"   Ожидалось: 'Нормальный вес'")

    print("\n3. Тестируем BMI=26 (высокий вес):")
    result3 = bmi_advice(26)
    print(f"   Результат: '{result3}'")
    print(f"   Ожидалось: 'Слишком высокий вес'")

    print("\n" + "=" * 50)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ:")
    # Проверяем, убил ли тест мутанта
    if result1 == "Слишком низкий вес":
        print("МУТАНТ УБИТ! Тесты обнаружили ошибку.")
    else:
        print("МУТАНТ ВЫЖИЛ! Тесты не обнаружили ошибку.")
        print(
            f"   При BMI=17 получили '{result1}' вместо 'Слишком низкий вес'")

except ImportError as e:
    print(f"Ошибка импорта: {e}")
except Exception as e:
    print(f"Ошибка: {e}")
