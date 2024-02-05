#!/usr/bin/python3
"""A class MyInt"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __equal__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __not_equal__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
