#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    "Amenity Class"
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    name = ""


    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
