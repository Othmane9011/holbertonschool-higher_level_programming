#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        """
        init square with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        return area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        get size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print square
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
