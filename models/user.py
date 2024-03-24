#!/usr/bin/python3
"""Sub classes for BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that's inherited from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
