#!/usr/bin/python3
"""
    A module that contains tests for the base_model module
"""
import os
import json
import unittest
import datetime
from models import storage
from models.base_model import BaseModel


class tests_BaseModel(unittest.TestCase):
    """
        A class for testing the BaseModel Class
    """

    def test_BaseModelType(self):
        """ Testing the type of an instance of BaseModel"""
        obj = BaseModel()
        self.assertTrue(type(obj) is BaseModel)
        self.assertIsInstance(obj, BaseModel)

    # Testing ID
    def test_ID(self):
        """ Testing the type of ID """
        obj = BaseModel()
        self.assertIsNotNone(obj.id, True)
        self.assertTrue(type(obj.id) is str)

    def test_UUID(self):
        """ Testing the uniquness of the ID """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj1.id != obj2.id)

    # Testing Attributes
    def test_NewAttrs(self):
        """ Testing the addition of new attributes and their types"""
        obj = BaseModel()
        obj.name = "Zidane"
        obj.age = 24
        obj.height = 178.2

        self.assertIsNotNone(obj.name, True)
        self.assertEqual(obj.name, "Zidane")
        self.assertTrue(type(obj.name) is str)

        self.assertIsNotNone(obj.age, True)
        self.assertEqual(obj.age, 24)
        self.assertTrue(type(obj.age) is int)

        self.assertEqual(obj.height, 178.2)
        self.assertIsNotNone(obj.height, True)
        self.assertTrue(type(obj.height) is float)

    def test_CreatedUpdated(self):
        """ Testing the created_at and updated_at attributes """
        obj = BaseModel()

        self.assertIsNotNone(obj.created_at, True)
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertIsInstance(obj.created_at, datetime.datetime)

        self.assertIsNotNone(obj.updated_at, True)
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    # Testing the __str__ method
    def test_STR(self):
        """ Testing the Str representation """
        tmp = BaseModel.__dict__.get('__str__')
        self.assertIsNotNone(tmp, True)

        obj = BaseModel()
        to_compare = f"[BaseModel] ({obj.id}) {obj.__dict__}"

        self.assertIsNotNone(str(obj), True)
        self.assertEqual(str(obj), to_compare)

    # Testing Save method
    def test_Save(self):
        """ Testing the save method """
        tmp = BaseModel.__dict__.get('save')
        self.assertIsNotNone(tmp, True)

        obj = BaseModel()
        time = obj.updated_at
        obj.save()

        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertTrue((obj.updated_at == time) is False)

    # Testing to_dict
    def test_ToDict(self):
        """ Testing the to_dict method """
        tmp = BaseModel.__dict__.get('to_dict')
        self.assertIsNotNone(tmp, True)

        obj1 = BaseModel()
        o_id = obj1.id
        o_create = obj1.created_at.isoformat()
        o_update = obj1.updated_at.isoformat()

        o_dict = {'id': o_id, 'created_at': o_create, 'updated_at': o_update,
                  '__class__': 'BaseModel'
                  }
        self.assertTrue(type(obj1.to_dict()) is dict)
        self.assertEqual(obj1.to_dict(), o_dict)

    def test_Kwargs(self):
        """ Testing the creation of an instance from a dictionary """
        o_id = "8a993912-5042-45f0-9362-b6a258e3ff92"
        tmp_create = "2024-03-20T14:43:04.244039"
        tmp_update = "2024-03-20T14:43:04.244043"
        tmp = {'id': o_id, 'created_at': tmp_create, 'updated_at': tmp_update,
               '__class__': 'Base', 'first_name': "Zidane", 'age': 24
               }

        obj = BaseModel(**tmp)

        self.assertIsNotNone(obj.id, True)
        self.assertTrue(type(obj.id) is str)
        self.assertEqual(obj.id, o_id)

        time = datetime.datetime.fromisoformat(tmp_create)
        self.assertIsNotNone(obj.created_at, True)
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertEqual(obj.created_at, time)

        time = datetime.datetime.fromisoformat(tmp_update)
        self.assertIsNotNone(obj.updated_at, True)
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertEqual(obj.updated_at, time)

        self.assertIsNotNone(obj.__class__, True)
        self.assertTrue(type(obj.__class__.__name__) is str)
        self.assertEqual(obj.__class__.__name__, 'BaseModel')

        self.assertIsNotNone(obj.first_name, True)
        self.assertTrue(type(obj.first_name) is str)
        self.assertEqual(obj.first_name, "Zidane")

        self.assertIsNotNone(obj.age, True)
        self.assertTrue(type(obj.age) is int)
        self.assertEqual(obj.age, 24)

        # Kwargs is empty case
        tmp = {}
        obj = BaseModel(**tmp)
        to_compare = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertIsNotNone(str(obj), True)
        self.assertEqual(str(obj), to_compare)

    def test_KwargsNew(self):
        """Testing the new method from storage if new inst not from a dict"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        obj = BaseModel()
        obj.save()
        with open("file.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertTrue(any(obj.id in key for key in data.keys()))