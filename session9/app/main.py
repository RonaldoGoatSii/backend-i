from fastapi import FastAPI, HTTPException
from app.api.schemas import MeetingCreate, MeetingRead, ErrorResponse

app = FastAPI(title="Meeting Note Assistant - Session 9")

# Banco de dados temporário
DB = []

@app.post(
    "/meetings", 
    response_model=MeetingRead, 
    status_code=201,
    responses={400: {"model": ErrorResponse}} # Challenge: Documentar erro no Swagger
)
def create_meeting(payload: MeetingCreate):
    # Simulação de criação com ID único
    new_meeting = MeetingRead(
        id=f"mtg-{len(DB) + 1}",
        **payload.model_dump()
    )
    DB.append(new_meeting)
    return new_meeting