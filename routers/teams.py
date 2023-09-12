from fastapi import APIRouter, Depends
from typing import Annotated
from database.db import engine, SessionLocal, Base
from database.models import Team
from schemas.teams import TeamUsersSchema
from sqlalchemy.orm import Session

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", status_code=201)
def create_team(user: TeamUsersSchema, db: db_dependency):
    try:
        team = Team(name=user.name)
        db.add(team)
        db.commit()
        return {"message": "Usuario creado correctamente"}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}
