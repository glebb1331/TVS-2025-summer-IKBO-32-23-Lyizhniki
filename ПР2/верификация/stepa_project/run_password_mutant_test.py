import sys
import os

sys.path.append(os.path.dirname(__file__))

try:
    from mutant_password_module import check_password_strength

    print("МУТАЦИОННОЕ ТЕСТИРОВАНИЕ PASSWORD MODULE")
    print("=" * 50)

    # Тестируем мутанта
    print("1. Тестируем очень сильный пароль:")
    strong_password = "Very$tr0ngP@ss!"
    result1 = check_password_strength(strong_password)
    print(f"   Пароль: {strong_password}")
    print(f"   Результат: '{result1}'")
    print(f"   Ожидалось: 'Очень сильный'")

    print("\n2. Тестируем слабый пароль:")
    weak_password = "short"
    result2 = check_password_strength(weak_password)
    print(f"   Пароль: {weak_password}")
    print(f"   Результат: '{result2}'")
    print(f"   Ожидалось: 'Слабый'")

    print("\n" + "=" * 50)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ:")

    if result1 == "Очень сильный":
        print("МУТАНТ УБИТ! Тесты обнаружили ошибку.")
    else:
        print("МУТАНТ ВЫЖИЛ! Тесты не обнаружили ошибку.")
        print(f"   Очень сильный пароль оценивается как '{result1}'")

except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
except Exception as e:
    print(f"❌ Ошибка: {e}")
