#!/usr/bin/python3
"""
Place class is one of the subclasses of BaseMode class
"""

from models import base_model
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(base_model.BaseModel):
    """BaseModel subclass"""
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0
    longitude: float = 0
    amenity_ids: list = []
