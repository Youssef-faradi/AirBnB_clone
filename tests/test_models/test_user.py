#!/usr/bin/python3
"""
    Unittest cases for models/user.py.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class in models/user.py.
    """
    def __init__(self, *args, **kwargs):
        """Initialization of User"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """First name test"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Last name test"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Email test"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Password test"""
        new = self.value()
        self.assertEqual(type(new.password), str)
