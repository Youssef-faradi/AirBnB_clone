#!/usr/bin/python3
"""
    Unittest cases for models/city.py.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class in models/city.py.
    """
    def __init__(self, *args, **kwargs):
        """Initialization test."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.name), str)
