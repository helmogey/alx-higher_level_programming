#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """ Square """
    def __init__(self, size=0, position=(0, 0)):
        """ size: private argument"""


        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            if self.__position[1] ==0:
                for i in range(0, self.__position[1]):
                    print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")
