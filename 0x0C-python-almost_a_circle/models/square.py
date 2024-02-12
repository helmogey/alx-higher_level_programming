#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value




    def update(self, *args, **kwargs):
        """
        Updates the Square's attributes based on provided arguments.

        Args:
            *args: A sequence of no-keyword arguments (tuples are not allowed).
                - 1st argument: id (integer)
                - 2nd argument: width (integer)
                - 3rd argument: height (integer)
                - 4th argument: x (integer)
                - 5th argument: y (integer)

        Raises:
            TypeError: If an argument is not of the expected type.
            ValueError: If an argument is not valid (e.g., negative width).
        """
        if args and len(args) !=0:
            for i, arg in enumerate(args):
                if i == 0:  # First argument for id (optional)
                    self.id = arg
                elif i == 1:  # Second argument for width (optional)
                    self.size = arg
                elif i == 2:  # Fourth argument for x (optional)
                    self.x = arg
                elif i == 3:  # Fifth argument for y (optional)
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value



    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}


    def __str__(self):
        """overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)