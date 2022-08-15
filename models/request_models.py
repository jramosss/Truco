from pydantic import Field, BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    identifier: str = Field(max_length=64, min_length=5)
    password: str = Field(max_length=64, min_length=8, regex="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$")
