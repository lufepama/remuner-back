from pydantic import BaseModel, validator
from typing import List

class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    status: bool

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value or "." not in value:
            raise ValueError("El campo 'email' debe contener el formato correcto")
        return value

class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    status: bool

class UserIdsListSchema(BaseModel):
    user_ids: List[int]