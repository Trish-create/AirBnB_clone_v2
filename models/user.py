#!/usr/bin/python3


from sqlalchemy import Column, String


from models.base_model import BaseModel, Base


class User(BaseModel):
    """User model,"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
