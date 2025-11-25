import pytest
from simpletools import add, sub, mul, div, mean, factorial


def test_add():
    assert add(2, 3) == 5


def test_div():
    assert div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        mean([])


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_type_errors():
    with pytest.raises(TypeError):
        add(1, "a")
    with pytest.raises(TypeError):
        factorial(3.5)
