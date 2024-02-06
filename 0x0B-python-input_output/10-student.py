#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """
    Represents a student with their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include. Defaults to None (all attributes).

        Returns:
            dict: A dictionary containing the specified student attributes.
        """

        data = {}
        if attrs is None:
            attrs = list(self.__dict__.keys())  # Include all attributes if attrs is None

        for attr_name in attrs:
            if hasattr(self, attr_name):
                data[attr_name] = getattr(self, attr_name)

        return data