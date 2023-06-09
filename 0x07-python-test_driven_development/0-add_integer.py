#!/usr/bin/python3
def add_integer(a, b=98):
    """adding two number
    Args:
        a: first number
        b: second number
    Return:
        result of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
