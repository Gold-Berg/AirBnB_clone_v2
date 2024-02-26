#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    state_id = ""
    name = ""


    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
