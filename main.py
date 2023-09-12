from fastapi import FastAPI
from typing import List, Annotated
from routers.users import router as users_router
from routers.teams import router as teams_router
from routers.integrations import router as integrations_router
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.declarative import declarative_base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Base = declarative_base()

#Add clients
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users")
app.include_router(teams_router, prefix="/teams")
app.include_router(integrations_router, prefix="/integrations")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_messages = []
    for error in exc.errors():

        print(error)
        field_name = error["loc"][0]
        error_message = error["msg"]
        error_messages.append(f"Error en el campo '{field_name}': {error_message}")
    return JSONResponse(status_code=400, content={"detail": error_messages})