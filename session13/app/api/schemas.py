from pydantic import BaseModel, Field
from typing import List

class MeetingCreate(BaseModel):
    title: str = Field(..., min_length=3)
    date: str
    owner: str
    participants: List[str] = Field(..., min_length=1)