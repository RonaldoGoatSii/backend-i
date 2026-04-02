from fastapi import FastAPI
from .models import Meeting, MeetingRequest, MeetingResponse
from datetime import datetime, date


api = FastAPI()


@api.get("/", response_model=list[Meeting])
def list_meetings(title:str = "", owner:str = "", date:datetime | None = None)-> list[Meeting]:
    return []


@api.post("/", response_model=MeetingResponse)
def create_meeting(meeting: MeetingRequest):
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