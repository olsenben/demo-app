"""Simple math helpers for agent fix loops."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b

# 6d2-cutover-smoke 2026-07-18T23:31:04.974523+00:00
