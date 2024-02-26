#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    place_id = ""
    user_id = ""
    text = ""


    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
