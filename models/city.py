#!/usr/bin/python3
"""
City class is one of the subclasses of BaseMode class
"""

from models import base_model
from models.state import State


class City(base_model.BaseModel):
    """BaseModel subclass"""
    state_id = ""
    name = ""
