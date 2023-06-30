#!/usr/bin/python3
""" Module that contains class rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes setter """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ area def """
        return self.height * self.width

    def display(self):
        """ display def """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """ str def """
        message = (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}").strip()
        return message

    def display(self):
        """ display def"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(self.__x * " " + "#" * self.__width)

    def update(self, *args, **kwargs):
        """def update attribut"""
        for key, value in kwargs.items():
            setattr(self, key, value)

        if len(args >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def to_dictionary(self):
        """dictionary"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }