#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """rectangle."""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """intialize rectangle."""

        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height


    @property
    def width(self):
        """return width."""
        return self.__width

    @width.setter
    def width(self, value):
        """set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """Return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the print shape """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """Return string Rectangle."""
        shape = "Rectangle(" + str(self.__width)
        shape += ", " + str(self.__height) + ")"
        return (shape)

    def __del__(self):
        """Print a delete message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
