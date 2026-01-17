""" define: 

    Item: with fields id, name, description (optional), and price.

    Item_Response: returns only id and name.

Use type hints and default values where needed.
"""
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    def Item_Response(self):
        return {"id": self.id, "name": self.name}