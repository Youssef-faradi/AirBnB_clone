#!/usr/bin/python3
"""
    Unittest cases for models/amenity.py.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class in models/amenity.py.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        new = self.value()
        self.assertEqual(type(new.name), str)
