from fastapi import FastAPI
from app.api.routers import action_items # Importa o teu novo router

app = FastAPI(title="Meeting Note Assistant")

# "Ligar os cabos" do router
app.include_router(action_items.router)

@app.get("/")
def health_check():
    return {"status": "online"}