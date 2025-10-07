import sys
import os

sys.path.append(os.path.dirname(__file__))

try:
    from mutant_matrix_module import matrix_addition

    print("МУТАЦИОННОЕ ТЕСТИРОВАНИЕ MATRIX MODULE")
    print("=" * 50)

    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("1. Тестируем сложение матриц:")
    result = matrix_addition(a, b)
    print(f"   Матрица A: {a}")
    print(f"   Матрица B: {b}")
    print(f"   Результат: {result}")
    print(f"   Ожидалось: [[6, 8], [10, 12]]")

    print("\n" + "=" * 50)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ:")

    if result == [[6, 8], [10, 12]]:
        print("МУТАНТ УБИТ! Тесты обнаружили ошибку.")
    else:
        print("МУТАНТ ВЫЖИЛ! Тесты не обнаружили ошибку.")
        print(f"   Получили {result} вместо [[6, 8], [10, 12]]")

except ImportError as e:
    print(f"Ошибка импорта: {e}")
except Exception as e:
    print(f"Ошибка: {e}")
