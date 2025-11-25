from __future__ import annotations
from typing import Iterable

__all__ = ["add", "sub", "mul", "div", "mean", "factorial"]


def _ensure_number(x):
    if not isinstance(x, (int, float)):
        raise TypeError(f"valor inválido: {x!r} não é número")
    return x


def add(a, b):
    _ensure_number(a)
    _ensure_number(b)
    return a + b


def sub(a, b):
    _ensure_number(a)
    _ensure_number(b)
    return a - b


def mul(a, b):
    _ensure_number(a)
    _ensure_number(b)
    return a * b


def div(a, b):
    _ensure_number(a)
    _ensure_number(b)
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b


def mean(values: Iterable[float]):
    seq = list(values)
    if len(seq) == 0:
        raise ValueError("mean() precisa de pelo menos um valor")

    total = 0.0
    count = 0
    for v in seq:
        _ensure_number(v)
        total += float(v)
        count += 1

    return total / count


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("factorial(n) espera inteiro não-negativo")
    if n < 0:
        raise ValueError("factorial(n) espera inteiro não-negativo")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result
