#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity model."""

    def __init__(self, *args, **kwargs):
        """Initialize an Amenity."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
