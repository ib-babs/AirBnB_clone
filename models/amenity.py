#!/usr/bin/python3
"""
Amenity class is one of the subclasses of BaseMode class
"""

from models import base_model


class Amenity(base_model.BaseModel):
    """BaseModel subclass"""
    name: str = ""
