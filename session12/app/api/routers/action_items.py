from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/action-items", tags=["Action Items"])

ITEMS = {1: {"task": "Rever Session 12", "status": "completed"}}

@router.get("/{item_id}")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return ITEMS[item_id]