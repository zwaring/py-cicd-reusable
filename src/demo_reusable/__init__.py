__all__ = ["add", "greet"]


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
