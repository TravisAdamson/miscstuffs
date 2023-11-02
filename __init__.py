#!/usr/bin/python3
"""Checks value of HBNB_TYPE_STORAGE
Used getenv directly without storing locally
and made only one reload after either storage is created"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
