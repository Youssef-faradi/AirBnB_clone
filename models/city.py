#!/usr/bin/python3
"""Sub classes for BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that's inherited from BaseModel."""
    state_id = ""
    name = ""
