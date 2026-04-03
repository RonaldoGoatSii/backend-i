from fastapi import FastAPI, HTTPException
from app.api.schemas import MeetingCreate, MeetingRead, ErrorResponse

app = FastAPI(title="Meeting Note Assistant - Session 9")

DB = []

@app.post(
    "/meetings", 
    response_model=MeetingRead, 
    status_code=201,
    responses={400: {"model": ErrorResponse}} 
)
def create_meeting(payload: MeetingCreate):
    new_meeting = MeetingRead(
        id=f"mtg-{len(DB) + 1}",
        **payload.model_dump()
    )
    DB.append(new_meeting)
    return new_meeting