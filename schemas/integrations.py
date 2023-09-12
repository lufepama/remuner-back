from pydantic import BaseModel, validator


class IntegrationCreateSchema(BaseModel):
    name: str
    type: str
    status: bool
