#!/usr/bin/python3
"""
    A module that contains the class FileStorage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "City": City,
           "State": State, "Amenity": Amenity, "Review": Review,
           "Place": Place
           }


class FileStorage():
    """
        A class that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            A public instance method that returns the dictrionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            A public instance method that sets in __objects the Obj
            with key <obj class name>.id
        """
        self.__objects.update({f"{obj.__class__.__name__}." + obj.id: obj})

    def save(self):
        """
            A public instance method that serializes __objects
            to the JSON file (path: __file_path)
        """
        tmp = {}
        for key in self.__objects:
            tmp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(tmp, f)

    def reload(self):
        """
            A public instance method that deserializes the JSON file to
            __objects (only if the JSON file exits otherwise it does nothing)
        """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                tp = json.load(f)
            for key in tp:
                self.__objects[key] = classes[tp[key]["__class__"]](**tp[key])
