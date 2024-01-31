#!/usr/bin/python3
"""locked class."""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes"""


    __slots__ = ["first_name"]
