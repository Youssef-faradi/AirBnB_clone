#!/usr/bin/python3
"""Sub classes for BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that's inherited from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
