""" 
    Objective: Create two endpoints to retrieve item(s).
    Instructions:
        In routes/items.py:
            Implement GET /items/: Return a list of all available items.
            Implement GET /items/{id}: Return an item by its ID using a path parameter.
                If not found, return 404 using HTTPException.
            Use response_model=Item_Response to hide sensitive data.
 """
from fastapi import APIRouter, HTTPException
from typing import List
from models.item import Item
router = APIRouter()
# Sample data
items_db = [
    Item(id=1, name="Item One", description="The first item", price=10.0),
    Item(id=2, name="Item Two", description="The second item", price=20.0),
    Item(id=3, name="Item Three", price=30.0),
]

@router.get("/items/", response_model=List[dict])
async def get_items():
    return [item.Item_Response() for item in items_db]

@router.get("/items/{id}", response_model=dict)
async def get_item(id: int):
    for item in items_db:
        if item.id == id:
            return item.Item_Response()
    raise HTTPException(status_code=404, detail="Item not found")

