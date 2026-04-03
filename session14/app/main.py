from fastapi import FastAPI
from app.api.routers import meetings, action_items

app = FastAPI(
    title="Meeting Note Assistant API",
    version="0.2.0"
)


app.include_router(meetings.router)
app.include_router(action_items.router)

@app.get("/dashboard/summary", tags=["dashboard"])
def get_summary():
    total_actions = sum(len(items) for items in action_items.ACTION_DB.values())
    
    return {
        "total_meetings": len(meetings.DB),
        "total_action_items": total_actions,
        "version": "0.2.0"
    }
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}