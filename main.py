#My first FastAPI project
from fastapi import FastAPI
from routers import items, users

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello world!"}

@app.get("/hello2")
def read_root():
    return {"Hello world again!"}

""" import and include the items router """
app.include_router(items.router)

app.include_router(users.router)