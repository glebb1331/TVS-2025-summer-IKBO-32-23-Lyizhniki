import pytest
from matrix_module import *


def test_matrix_addition():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = matrix_addition(a, b)
    assert result == [[6, 8], [10, 12]]

    with pytest.raises(ValueError):
        matrix_addition([[1, 2]], [[1]])


def test_matrix_multiplication():
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 2]]
    result = matrix_multiplication(a, b)
    assert result == [[4, 4], [10, 8]]


def test_matrix_transpose():
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = matrix_transpose(matrix)
    assert result == [[1, 4], [2, 5], [3, 6]]


def test_is_square_matrix():
    assert is_square_matrix([[1, 2], [3, 4]])
    assert not is_square_matrix([[1, 2, 3], [4, 5, 6]])


def test_matrix_determinant():
    matrix = [[2, 0], [0, 2]]
    assert matrix_determinant(matrix) == 4
