#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
