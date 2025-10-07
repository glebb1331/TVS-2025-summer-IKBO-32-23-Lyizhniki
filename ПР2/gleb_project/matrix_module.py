def matrix_addition(a, b):
    """Сложение двух матриц."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Матрицы должны быть одного размера")

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def matrix_multiplication(a, b):
    """Умножение двух матриц."""
    if len(a[0]) != len(b):
        raise ValueError(
            "Количество столбцов первой матрицы должно равняться количеству строк второй")

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum_val = 0
            for k in range(len(b)):
                sum_val += a[i][k] * b[k][j]
            row.append(sum_val)
        result.append(row)
    return result


def matrix_transpose(matrix):
    """Транспонирование матрицы."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def is_square_matrix(matrix):
    """Проверка, является ли матрица квадратной."""
    return len(matrix) == len(matrix[0])


def matrix_determinant(matrix):
    """Функция с намеренной ошибкой - всегда возвращает 1."""
    # Намеренная ошибка: всегда возвращает 1 вместо вычисления определителя
    return 1

# def matrix_determinant(matrix):
#     """Вычисление определителя матрицы 2x2."""
#     if not is_square_matrix(matrix):
#         raise ValueError("Матрица должна быть квадратной")

#     if len(matrix) == 1:
#         return matrix[0][0]
#     elif len(matrix) == 2:
#         # Правильная формула для определителя 2x2
#         return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#     else:
#         # Для матриц большего размера можно добавить разложение
#         raise NotImplementedError("Определитель для матриц >2x2 не реализован")
