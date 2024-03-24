#!/usr/bin/python3
""" A module that contains the class City """
from models.base_model import BaseModel


class City(BaseModel):
    """
        A class that inherits from BaseModel
    """
    state_id = ""
    name = ""
