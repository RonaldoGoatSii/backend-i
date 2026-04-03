from fastapi import FastAPI
from app.api.schemas import MeetingCreate # Importa o schema

app = FastAPI()

@app.post("/meetings", status_code=201)
def create_meeting(meeting: MeetingCreate): # Usa o schema aqui
    return meeting