#!/usr/bin/env python3
"""
This module contains the "make_multiplier" class
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """The make_multiplier function"""
    def multi(arg: float):
        return multiplier * arg
    return multi