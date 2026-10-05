#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review model."""

    def __init__(self, *args, **kwargs):
        """Initialize a Review."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("text", "")
