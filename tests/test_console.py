#!/usr/bin/python3
"""
    Unittest cases for console.py.
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import os
from models.engine.file_storage import FileStorage
from models import storage


class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNBCommand class in console.py.
    """
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
