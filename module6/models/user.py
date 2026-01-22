from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr, Field

Base = declarative_base()

class User(Base):    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index = True)
    username = Column(String(50), unique=True, nullable=False, index = True)
    fullname = Column(String)
    email = Column(String(100), unique=True, nullable=False, index = True)
    hashed_password = Column(String, nullable=True)
    
    
    github_id = Column(String(100), unique=True, nullable=True)
    avatar_url = Column(String, nullable=True)
    auth_provider = Column(String(50), nullable=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', fullname='{self.fullname}', email='{self.email}')>"
    
class UserRequest(BaseModel):
    username: str = Field(min_length = 3, max_length = 50) 
    fullname: str = Field(min_length = 3, max_length = 100)
    email: EmailStr
    password: str = Field(min_length = 8)

class UserResponse(BaseModel):
    username: str
    email: str
    
class UserLoginRequest(BaseModel):
    username: str
    password: str
    
class UserLoginResponse(BaseModel):
    message: str
    username: str
    access_token: str
    access_token_type: str = "bearer"