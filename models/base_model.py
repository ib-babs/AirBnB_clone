#!/usr/bin/python3
"""
BaseModel class is a parent class inherited by subclasses
"""

from datetime import datetime as dt
from uuid import uuid4
import models


class BaseModel():
    """BaseModel Definition"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing BaseModel class"""
        date_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs != {}:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = dt.strptime(
                        kwargs["created_at"], date_fmt)
                elif "updated_at" == key:
                    self.updated_at = dt.strptime(
                        kwargs["updated_at"], date_fmt)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)

        else:
            self.created_at = dt.now()
            self.id = str(uuid4())
            self.updated_at = dt.now()
            models.storage.new(self)

    def save(self) -> None:
        """Updates the public instance attribute\
            `updated_at` with the current datetime"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    def __str__(self) -> str:
        """Return string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self) -> str:
        """Return string repr"""
        return (self.__str__())
