from pydantic import BaseModel
from typing import List

class TeamUsersCreateSchema(BaseModel):
    name: str

class TeamAddUserSchema(BaseModel):
    team_id: int
    user_id: int

class TeamIdsListSchema(BaseModel):
    team_ids: List[int]