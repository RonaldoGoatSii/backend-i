from fastapi import APIRouter, Query

router = APIRouter(prefix="/meetings", tags=["action-items"])

ACTION_DB = {}

@router.get("/{meeting_id}/action-items")
def list_action_items(meeting_id: str):
    return ACTION_DB.get(meeting_id, [])