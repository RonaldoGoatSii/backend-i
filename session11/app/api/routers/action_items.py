from fastapi import APIRouter, HTTPException
from app.api.schemas import ActionItemCreate, ActionItemRead
from typing import List

router = APIRouter(prefix="/meetings", tags=["action-items"])

ACTION_DB: dict[str, list[dict]] = {}

@router.post("/{meeting_id}/action-items", response_model=ActionItemRead)
def create_action_item(meeting_id: str, payload: ActionItemCreate):
    existing_items = ACTION_DB.get(meeting_id, [])
    new_id = str(len(existing_items) + 1)

    item_data = payload.model_dump()
    item_data["id"] = new_id

    ACTION_DB.setdefault(meeting_id, []).append(item_data)
    
    return item_data

@router.get("/{meeting_id}/action-items", response_model=List[ActionItemRead])
def list_action_items(meeting_id: str):
    return ACTION_DB.get(meeting_id, [])