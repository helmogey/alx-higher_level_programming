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

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return data
