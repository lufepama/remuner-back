from fastapi import APIRouter, Depends
from typing import List, Annotated
from database.db import engine, SessionLocal, Base
from database.models import User
from schemas.users import UserCreateSchema, UserIdsListSchema
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
def create_user(user: UserCreateSchema, db: db_dependency):
    try:
        user = User(first_name=user.first_name, last_name=user.last_name, email=user.email, status=user.status)
        db.add(user)
        db.commit()
        return {"message": "Usuario creado correctamente", "data": user.id ,"success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}

@router.get("/", status_code=200)
def get_users(db: db_dependency):
    try:
        query = db.query(User).all()
        return {"message": "Todo ha ido bien", "data": query, "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}

@router.delete("/", status_code=200)
def delete_users(users_list: UserIdsListSchema, db: db_dependency):
    try:
        for user_id in users_list.user_ids:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                db.delete(user)
        db.commit()
        return {"message": "Usuarios eliminados correctamente", "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}