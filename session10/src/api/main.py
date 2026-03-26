from fastapi import FastAPI
from .models import Meeting, MeetingRequest, MeetingResponse
from datetime import datetime, date


api = FastAPI()


@api.get("/", response_model=list[Meeting])
def list_meetings(title:str = "", owner:str = "", date:datetime | None = None)-> list[Meeting]:
    return []


@api.post("/", response_model=MeetingResponse)
def create_meeting(meeting: MeetingRequest):
    # Service (request ao Docker model para retornar o resumo
    # Temos de fazer um prompt para o modelo percebem que tem de fazer um resumo das notas
    # Depois temos de guardar nos respetivos ficheiros (conforme foi feito com o typer)
    # E retornar o id para o user
    response = requests.post(
        "https://ollama:11434/api/generate",
        data=(
            "model":"smollm2:135m",
            "prompt":f"faz um resumo destas notas em bullet points <NOTE>{meeting.notes}</NOTES>"
        )
        
        )



@api.get("/{meeting_id}", response_model= Meeting)
def get_meeting():
    ...

















# @api.get("/shop")
# def list_product():
#     ...


# @api.get("/shop/{category}")
# def list2_product(category:str):
#     return f"category - {category}"

# @api.get("/shop/{category}/{product}")
# def list3_product(category:str, product:str):
#     return f"category - -{category} || product - {product}"

# @api.post("/shop")
# def list4_product():
#     ...