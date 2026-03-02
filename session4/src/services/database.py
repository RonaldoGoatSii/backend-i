import json
import os
from data.models import Meeting
from uuid import uuid4
from dataclasses import asdict

# Caminhos relativos ao local onde corres o programa (raiz da session4)
BASE_PATH = "meetings" 
JSON_FILE = "src/data/meetings.json"

def create(meeting: Meeting):
    # 1. Garante que as pastas existem
    os.makedirs(BASE_PATH, exist_ok=True)
    os.makedirs("src/data", exist_ok=True)
    
    # 2. Criar o ficheiro Markdown (ID único)
    md_id = str(uuid4())
    filename = f"{BASE_PATH}/{md_id}.md"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(meeting))

    # 3. Atualizar o Índice JSON
    data = load_all()
    
    meeting_dict = asdict(meeting)
    meeting_dict["id"] = md_id  
    
    data.append(meeting_dict)
    
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_all():
    """Lê todas as reuniões do JSON"""
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def search(query: str):
    """Procura no JSON pelo título"""
    all_data = load_all()
    return [m for m in all_data if query.lower() in m['title'].lower()]