from pydantic import BaseModel, Field
from typing import List

class MeetingBase(BaseModel):
    title: str = Field(..., min_length=3)
    date: str
    owner: str
    participants: List[str] = Field(..., min_length=1)

class MeetingCreate(MeetingBase):
    pass

class MeetingRead(MeetingBase):
    id: str

class DashboardSummary(BaseModel):
    total_meetings: int
    total_action_items: int
    status: str