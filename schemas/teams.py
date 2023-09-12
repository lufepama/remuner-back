from pydantic import BaseModel


class TeamUsersCreateSchema(BaseModel):
    name: str

class TeamAddUserSchema(BaseModel):
    team_id: int
    user_id: int