from fastapi import APIRouter, Depends
from typing import List, Annotated
from database.db import engine, SessionLocal, Base
from database.models import User
from schemas.users import UserCreateSchema
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
def create_integration():
    pass