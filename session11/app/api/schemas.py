from pydantic import BaseModel, Field
from datetime import date

class ActionItemCreate(BaseModel):
    # Challenge: O 'min_length=2' garante que o owner não seja vazio
    description: str = Field(..., min_length=3, description="O que tem de ser feito")
    owner: str = Field(..., min_length=2, description="Quem vai fazer")
    # Challenge: Usar 'date' em vez de 'str' valida automaticamente a data
    due_date: date 

class ActionItemRead(ActionItemCreate):
    id: str