#!/usr/bin/python3
"""
    Unittest cases for models/state.py.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class in models/state.py.
    """
    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
