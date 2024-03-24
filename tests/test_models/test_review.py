#!/usr/bin/python3
"""
    Unittest cases for models/review.py.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class in models/review.py.
    """
    def __init__(self, *args, **kwargs):
        """Initialization test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ID test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """User ID test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Text test"""
        new = self.value()
        self.assertEqual(type(new.text), str)
