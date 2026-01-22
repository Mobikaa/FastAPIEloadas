from fastapi import FastAPI
from database import engine
from models.user import Base
from routers import users, auth
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router, prefix = "/users", tags = ["Users"])
app.include_router(auth.router, prefix = "/auth", tags = ["Auth"])

