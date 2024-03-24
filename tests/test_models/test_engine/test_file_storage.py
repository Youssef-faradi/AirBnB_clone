#!/usr/bin/python3
""" A module that contains tests for the file_storage module """
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class tests_FileStorage(unittest.TestCase):
    """ A test class for the FileStorage class """

    def setUp(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

        FileStorage._FileStorage__objects = {}

    def test_FileStorage(self):
        """ Testing the integrity of FileStorage """
        obj = FileStorage()
        path = "file.json"

        self.assertIsNotNone(obj, True)
        self.assertTrue(type(obj) is FileStorage)
        self.assertTrue(os.path.exists(path) is False)
        self.assertIsNotNone(FileStorage._FileStorage__file_path, True)
        self.assertTrue(FileStorage._FileStorage__file_path == "file.json")
        self.assertIsNotNone(FileStorage._FileStorage__objects, True)

    def test_All(self):
        """ Testing the method all """
        tmp = FileStorage.__dict__.get('all')
        self.assertIsNotNone(tmp, True)

        obj = FileStorage()

        self.assertTrue(type(obj.all()) is dict)
        self.assertEqual(obj.all(), FileStorage._FileStorage__objects)

    def test_New(self):
        """ Testing the method new """
        tmp = FileStorage.__dict__.get('new')
        self.assertIsNotNone(tmp, True)

        obj = FileStorage()
        Base = BaseModel()
        objects = FileStorage._FileStorage__objects

        obj.new(Base)
        self.assertTrue(f"BaseModel.{Base.id}" in objects.keys())

    def test_Save(self):
        """ Testing the method save """
        tmp = FileStorage.__dict__.get('save')
        self.assertIsNotNone(tmp, True)

        obj = FileStorage()
        Base = BaseModel()

        if os.path.exists("file.json"):
            os.remove("file.json")
            obj.new(Base)
            obj.save()
            with open("file.json", 'r', encoding="utf-8") as f:
                data = f.readline()
                objects = FileStorage._FileStorage__objects
                self.assertTrue(f"{Base.id}" in data)
        else:
            obj.new(Base)
            obj.save()
            with open("file.json", 'r', encoding="utf-8") as f:
                data = f.readline()
                objects = FileStorage._FileStorage__objects
                self.assertTrue(f"{Base.id}" in data)

    def test_Reload(self):
        """ testing the method Reload """
        tmp = FileStorage.__dict__.get('reload')
        self.assertIsNotNone(tmp, True)

        objects = FileStorage._FileStorage__objects
        obj = FileStorage()
        obj.new(BaseModel())
        obj.save()
        obj.reload()
        self.assertEqual(obj._FileStorage__objects, objects)