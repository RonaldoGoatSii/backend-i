from pydantic import BaseModel, Field
from datetime import date

class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=3, description="O que tem de ser feito")
    owner: str = Field(..., min_length=2, description="Quem vai fazer")
    due_date: date 

class ActionItemRead(ActionItemCreate):
    id: str