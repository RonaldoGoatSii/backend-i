from fastapi import APIRouter, Query
from typing import List

router = APIRouter(prefix="/meetings", tags=["action-items"])

ACTION_DB = {
    "mtg-1": [
        {"id": "1", "description": "Fazer café", "owner": "Jorge", "due_date": "2026-04-01"},
        {"id": "2", "description": "Ata da reunião", "owner": "Ana", "due_date": "2026-03-31"},
        {"id": "3", "description": "Rever código", "owner": "Jorge", "due_date": "2026-04-02"},
    ]
}

@router.get("/{meeting_id}/action-items")
def list_action_items(
    meeting_id: str,
    owner: str | None = None,
    limit: int = Query(default=10, ge=1, le=50),
    offset: int = Query(default=0, ge=0)
):
    items = ACTION_DB.get(meeting_id, [])
    
    items = sorted(items, key=lambda x: (x["due_date"], x["id"]))

    if owner:
        items = [item for item in items if item["owner"].lower() == owner.lower()]

    total = len(items)
    paginated_items = items[offset : offset + limit]

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "items": paginated_items
    }