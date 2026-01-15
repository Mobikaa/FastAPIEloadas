#My first FastAPI project
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello world!"}

@app.get("/hello2")
def read_root():
    return {"Hello world again!"}