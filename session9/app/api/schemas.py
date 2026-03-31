from pydantic import BaseModel, Field
from typing import List

# Challenge: Esquema padrão para erros 4xx
class ErrorResponse(BaseModel):
    detail: str
    code: str

class MeetingCreate(BaseModel):
    # Exercise: Título com mínimo de 3 caracteres
    title: str = Field(..., min_length=3, example="Retro Semanal")
    date: str = Field(..., example="2026-03-31")
    owner: str = Field(..., min_length=2, example="Jorge")
    # Exercise: Lista de participantes não pode estar vazia
    participants: List[str] = Field(..., min_length=1, description="Pelo menos um participante é obrigatório")

class MeetingRead(MeetingCreate):
    id: str