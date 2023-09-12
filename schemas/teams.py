from pydantic import BaseModel, validator
from typing import List, Optional
from .users import UserSchema


class TeamUsersSchema(BaseModel):
    name: str