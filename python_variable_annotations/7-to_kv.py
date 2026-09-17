#!/usr/bin/env python3
"""Module for converting a string and number into a key-value tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string and the square of the number."""
    return (k, v ** 2)
