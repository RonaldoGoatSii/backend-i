import json
import os
from data.models import Meeting
from uuid import uuid4
from dataclasses import asdict

BASE_PATH = "meetings"
JSON_FILE = "data/meetings.json"

def create(meeting: Meeting):
    # --- Passo 1: Criar o ficheiro Markdown (o teu código atual) ---
    os.makedirs(BASE_PATH, exist_ok=True)
    md_id = str(uuid4())
    filename = f"{BASE_PATH}/{md_id}.md"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(meeting))

    # --- Passo 2: Atualizar o Índice JSON ---
    os.makedirs("data", exist_ok=True)
    
    # 1. Carregar reuniões existentes
    data = load_all()
    
    # 2. Converter objeto para dicionário e adicionar o ID do ficheiro MD
    meeting_dict = asdict(meeting)
    meeting_dict["id"] = md_id  # Guardamos o ID para saberes qual MD abrir depois
    
    data.append(meeting_dict)
    
    # 3. Gravar de volta no JSON
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_all():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []