#!/usr/bin/python3
"""
    A module that contains the class BaseModel
"""
import json
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    A class that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Class constructor

            Args:
                *args: Not used
                **kwargs: Contains the keys/value of an instance
        """
        from models import storage
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            A method that returns the string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
                A public instance method that updates the public instance
                attribute updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            A methor that returns the dictionary containing all keys/values
            from __dict__ of the instance
        """
        dict_list = []
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                dict_list.append((f"{k}", v.isoformat()))
            else:
                dict_list.append((f"{k}", v))
        dict_list.append((f"__class__", self.__class__.__name__))
        return dict(dict_list)
