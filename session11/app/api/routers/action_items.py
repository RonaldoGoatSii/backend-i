from fastapi import APIRouter, HTTPException
from app.api.schemas import ActionItemCreate, ActionItemRead
from typing import List

router = APIRouter(prefix="/meetings", tags=["action-items"])

# Banco de dados temporário em memória
# Estrutura: {"id_da_reuniao": [lista_de_tarefas]}
ACTION_DB: dict[str, list[dict]] = {}

@router.post("/{meeting_id}/action-items", response_model=ActionItemRead)
def create_action_item(meeting_id: str, payload: ActionItemCreate):
    # 1. Criar um ID simples baseado no tamanho da lista
    existing_items = ACTION_DB.get(meeting_id, [])
    new_id = str(len(existing_items) + 1)
    
    # 2. Transformar o Pydantic em dicionário e adicionar o ID
    item_data = payload.model_dump()
    item_data["id"] = new_id
    
    # 3. Guardar no "banco de dados"
    ACTION_DB.setdefault(meeting_id, []).append(item_data)
    
    return item_data

@router.get("/{meeting_id}/action-items", response_model=List[ActionItemRead])
def list_action_items(meeting_id: str):
    return ACTION_DB.get(meeting_id, [])