from dotenv import load_dotenv
from fastapi import FastAPI, logger
from database import engine
from models.user import Base
from routers import users

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix = "/users", tags = ["Users"])

