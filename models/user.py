#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    email = ''
    password = ''
    first_name = ''
    last_name = ''


    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
