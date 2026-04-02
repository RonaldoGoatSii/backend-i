from pydantic import BaseModel, Field
from typing import List
from datetime import date

class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=3)
    owner: str = Field(..., min_length=2)
    due_date: date 

class ActionItemRead(ActionItemCreate):
    id: str

class ErrorResponse(BaseModel):
    detail: str
    code: str