#!/usr/bin/python3
"""Define the base of all other classes"""

from json import dumps, loads
import json


class Base:
    """Base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file."""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
        """ from json """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        class_name = []
        with open(filename, "r") as read_file:
            file = read_file.read()
            _list = cls.from_json_string(file)
            for i in _list:
                class_name.append(cls.create(**i))
            return class_name
