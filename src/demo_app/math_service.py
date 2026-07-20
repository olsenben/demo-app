"""Simple math helpers for agent fix loops."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b

# demo-e2e-6d 2026-07-20T00:23:36.264990+00:00 3529dad9

# demo-e2e-6f2 2026-07-20T00:23:41.609030+00:00 3529dad9
