from fastapi import APIRouter, Depends
from typing import List, Annotated
from database.db import engine, SessionLocal, Base
from database.models import Integration
from schemas.integrations import IntegrationCreateSchema, IntegrationsIdsListSchema
from sqlalchemy.orm import Session
import utils

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
def create_integration(integration: IntegrationCreateSchema, db: db_dependency):
    try:
        token = utils.generate_random_token()
        integration_query = Integration(name=integration.name, type=integration.type, token=token, status=integration.status)
        db.add(integration_query)
        db.commit()
        return {"message": "Integracion creada correctamente", "data": {"id": integration_query.id, "token": token}, "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}

@router.get("/", status_code=200)
def get_integrations(db: db_dependency):
    try:
        query = db.query(Integration).all()
        return {"message": "Todo ha ido bien", "data": query, "success": True}
    except Exception as e:
        return {"message": f"Algo ha ido mal...{str(e)}"}

@router.delete("/", status_code=200)
def delete_integrations(integration_list: IntegrationsIdsListSchema, db: db_dependency):
    for user_id in integration_list.integration_ids:
        user = db.query(Integration).filter(Integration.id == user_id).first()
        if user:
            db.delete(user)
    db.commit()
    return {"message": "Integraciones eliminadas correctamente", "success": True}    
