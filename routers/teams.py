from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from database.db import engine, SessionLocal, Base
from database.models import Team, User
from schemas.teams import TeamUsersCreateSchema, TeamAddUserSchema, TeamIdsListSchema
from schemas.users import UserSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

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
def create_team(user: TeamUsersCreateSchema, db: db_dependency):
    try:
        team = Team(name=user.name)
        db.add(team)
        db.commit()
        return {"message": "Equipo creado correctamente", "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}

@router.get("/", status_code=200)
def get_teams(db: db_dependency):
    try:
        query = db.query(Team).all()
        return {"message": "Todo ha ido bien", "data": query, "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}

@router.delete("/", status_code=200)
def delete_teams(teams_list: TeamIdsListSchema, db: db_dependency):
    for user_id in teams_list.team_ids:
        user = db.query(Team).filter(Team.id == user_id).first()
        if user:
            db.delete(user)
    db.commit()
    return {"message": "Equipos eliminados correctamente", "success": True}



@router.post("/add-user", status_code=201)
def add_user_to_team(data: TeamAddUserSchema, db: db_dependency):
    team = db.query(Team).filter(Team.id == data.team_id).first()
    user = db.query(User).filter(User.id == data.user_id).first()
    
    if not team or not user:
        raise HTTPException(status_code=400, detail="Equipo o usuario no encontrado")
    try:
        user.team = team
        db.commit()
        db.refresh(user)
        return {"message": "Equipo creado correctamente", "success": True}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="El usuario ya existe en el equipo")

@router.get("/{team_id}/user-list", status_code=200)
def get_user_list_in_team(team_id: int, db: db_dependency):
    try:
        team = db.query(Team).filter(Team.id == team_id).first()
        return {"message": "Todo ha ido bien", "data": team.users, "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}