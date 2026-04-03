from fastapi import APIRouter, HTTPException, Query
from app.api.schemas import MeetingCreate, MeetingRead

router = APIRouter(prefix="/meetings", tags=["meetings"])

# Simulação de base de dados
DB = {}

@router.post("", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate):
    meeting_id = f"mtg-{len(DB) + 1}"
    new_meeting = MeetingRead(id=meeting_id, **payload.model_dump())
    DB[meeting_id] = new_meeting.model_dump()
    return new_meeting

@router.get("")
def list_meetings(owner: str | None = None):
    items = list(DB.values())
    if owner:
        items = [m for m in items if m["owner"] == owner]
    return items