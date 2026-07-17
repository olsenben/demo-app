from demo_app.math_service import add, divide, multiply


def test_add() -> None:
    assert add(2, 3) == 5


def test_divide() -> None:
    assert divide(10, 2) == 5.0


def test_divide_by_zero() -> None:
    try:
        divide(1, 0)
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_multiply() -> None:
    assert multiply(3, 4) == 12


def test_6f2_intentional_fail() -> None:
    assert False, "stage4 intentional test_failure for repair_allowed"
