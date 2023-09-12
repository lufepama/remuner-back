from pydantic import BaseModel
from typing import List

class IntegrationCreateSchema(BaseModel):
    name: str
    type: str
    status: bool

class IntegrationsIdsListSchema(BaseModel):
    integration_ids: List[int]
