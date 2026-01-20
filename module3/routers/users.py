""" Instructions:

    In routers/users.py:

        GET /users/: Return all users.

        POST /users/: Create a user.
            Return 400 if the id already exists.
            Respond with a User_Response.

        GET /users/{id}: Return a full user by ID or raise 404.

        DELETE /users/{id}: Remove user by ID or raise 404.
 """
from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User

router = APIRouter()

""" gernerate 10 users as sample data """
users = [
    User(id=1, username="john_doe", email="john@example.com", full_name="John Doe"),
    User(id=2, username="jane_smith", email="jane@example.com", full_name="Jane Smith"),
    User(id=3, username="bob_johnson", email="bob@example.com", full_name="Bob Johnson"),
    User(id=4, username="alice_williams", email="alice@example.com", full_name="Alice Williams"),
    User(id=5, username="charlie_brown", email="charlie@example.com", full_name="Charlie Brown"),
    User(id=6, username="diana_miller", email="diana@example.com", full_name="Diana Miller"),
    User(id=7, username="edward_davis", email="edward@example.com", full_name="Edward Davis"),
    User(id=8, username="frank_rodriguez", email="frank@example.com", full_name=None),
    User(id=9, username="grace_martinez", email="grace@example.com", full_name=None),
    User(id=10, username="henry_gonzalez", email="henry@example.com", full_name=None),
]

@router.get("/users/", response_model=List[dict])
async def get_users():
    return [user.User_Response() for user in users]

@router.post("/users/", response_model=dict)
async def create_user(user: User):
    for existing_user in users:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    users.append(user)
    return user.User_Response()

@router.get("/users/{id}", response_model=User)
async def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{id}", response_model=dict)
async def delete_user(id: int):
    for index, user in enumerate(users):
        if user.id == id:
            del users[index]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")