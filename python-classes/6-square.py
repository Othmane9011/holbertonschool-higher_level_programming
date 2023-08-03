#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init square with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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
            return
        for k in range(0, self.position[1]):
            print()
        for i in range(0, self.__size):
            for p in range(0, self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        """
        position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
