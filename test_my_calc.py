import pytest

from my_calc import *


def test_sum_num():
    """Тест для функции сложения"""
    result = sum(5, 7)
    assert result == 12, "Функция сложения должна возвращать  значение 12"
    result = sum(1.5, 2.5)
    assert result == 4, "Функция сложения должна возвращать  значение 4"
    with pytest.raises(TypeError):
        sum("5", 7)


def test_minus_num():
    """Тест для функции вычитания"""
    result = minus(15, 17)
    assert result == -2, "Функция вычитания должна возвращать  значение -2"
    result = minus(17.5, 15.5)
    assert result == 2, "Функция вычитания должна возвращать  значение 2"
    with pytest.raises(TypeError):
        minus(15, "17")


def test_multi_num():
    """Тест для функции умножения"""
    result = multi(15, 0)
    assert result == 0, "Функция вычитания должна возвращать  значение 0"
    result = multi(3, 2)
    assert result == 6, "Функция вычитания должна возвращать  значение 6"
    result = multi(17.2, 15.7)
    assert result == 270.03999999999996, "Функция вычитания должна возвращать  значение 270.03999999999996"
    with pytest.raises(TypeError):
        multi("15", "17")


def test_division_num():
    """Тест для функции деления"""
    result = division(15, 5)
    assert result == 3, "Функция вычитания должна возвращать  значение 3"
    result = division(30.1, 2)
    assert result == 15.05, "Функция вычитания должна возвращать  значение 15.05"
    with pytest.raises(ValueError):
        division(10, 0)
    with pytest.raises(TypeError):
        division("15", "17")
