#!/usr/bin/python3
"""
Review class is one of the subclasses of BaseMode class
"""

from models import base_model
from models.place import Place
from models.user import User


class Review(base_model.BaseModel):
    """BaseModel subclass"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
