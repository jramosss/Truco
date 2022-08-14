from pydantic import Field, BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    username: Optional[str] = Field(max_length=20, min_length=5)
    email: Optional[str] = Field(regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password: str = Field(max_length=64, min_length=8, regex="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$")
