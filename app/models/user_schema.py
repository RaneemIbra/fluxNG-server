from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegisterRequestSchema(BaseModel):
    email: EmailStr
    password: str

class UserProfileResponseSchema(BaseModel):
    id: str
    email: Optional[EmailStr] = None
    role: Optional[str] = None