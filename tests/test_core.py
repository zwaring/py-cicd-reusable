import pytest

from demo_reusable import add, greet


def test_add() -> None:
    assert add(2, 3) == 5


def test_greet() -> None:
    assert greet("ci") == "Hello, ci!"


def test_greet_empty() -> None:
    with pytest.raises(ValueError):
        greet("")
