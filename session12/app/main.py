from fastapi import FastAPI
from app.api.routers import action_items

app = FastAPI(title="Meeting Note Assistant")

app.include_router(action_items.router)

@app.get("/")
def health_check():
    return {"status": "online"}