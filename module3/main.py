#My first FastAPI project
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello world!"}

@app.get("/hello2")
def read_root():
    return {"Hello world again!"}



class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    
#Create 10 sample items
items = [
    Item(name="Laptop", price=999.99, in_stock=True),
    Item(name="Mouse", price=25.50, in_stock=False),
    Item(name="Keyboard", price=75.00, in_stock=True),
    Item(name="Monitor", price=299.99, in_stock=True),
    Item(name="Headphones", price=149.99, in_stock=False),
    Item(name="Tablet", price=349.99, in_stock=True),
    Item(name="Smartphone", price=699.99, in_stock=False),
    Item(name="Charger", price=15.00, in_stock=True),
    Item(name="Case", price=20.00, in_stock=False),
    Item(name="Screen Protector", price=10.00, in_stock=True)
]

#generate a get endpoint to fetch all items
@app.get("/items/")
def get_items():
    return items

#generate a post endpoint to upload items
@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item

""" Objective: Implement a GET /items/ endpoint that supports pagination.
Instructions:
Accept query parameters: skip (default: 0), limit (default: 10)
Return a slice of the items list from skip to skip + limit.
Bonus:
Add optional filters (e.g., in_stock=true) """
@app.get("/items/paginated/")
def get_paginated_items(skip: int = 0, limit: int = 10, in_stock: bool = None):
    filtered_items = items
    if in_stock is not None:
        filtered_items = [item for item in items if item.in_stock == in_stock]
    return filtered_items[skip : skip + limit]