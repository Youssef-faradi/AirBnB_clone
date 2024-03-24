#!/usr/bin/python3
"""Creates an unique FileStorage instance for AirBnB clone application."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
