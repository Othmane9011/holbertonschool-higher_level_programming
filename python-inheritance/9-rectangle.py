#!/usr/bin/python3
""""Rectangle heritage"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area define """
        return self.__width * self.__height

    def __str__(self):
        """ dunder __str__define """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
