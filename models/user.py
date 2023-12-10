#!/usr/bin/python3
"""
User class is one of the subclasses of BaseMode class
"""

from models import base_model


class User(base_model.BaseModel):
    """BaseModel subclass"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
