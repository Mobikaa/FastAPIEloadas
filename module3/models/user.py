""" Instructions:

    In models/user.py:

        Create User with:
            Validated username (3–50 chars)
            Validated email (regex pattern)
            Optional full_name (max 100 chars)
            Default is_active=True

        Define User_Response to include only id and full_name.
 """
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: bool = True

    def User_Response(self):
        return {"id": self.id, "full_name": self.full_name}