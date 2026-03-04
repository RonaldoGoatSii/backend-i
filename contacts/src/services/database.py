from dataclasses import asdict
import json
from pathlib import Path
from data.models import contactos, ContactInfo
from uuid import uuid4
import os

BASE_PATH = "contacts" 
JSON_FILE = "contacts/contacts.json"

def create(contact: contactos):
    """Cria um novo contacto em Markdown e atualiza o índice JSON"""

    os.makedirs(BASE_PATH, exist_ok=True)
    os.makedirs("src/data", exist_ok=True)
    

    contact_id = str(uuid4())
    filename = f"{BASE_PATH}/{contact_id}.md"
    
    with open(filename, "w", encoding="utf-8") as f:

        f.write(str(contact))

    all_contacts = load_all()
    
    contact_data = asdict(contact)
    contact_data["id"] = contact_id 
    
    all_contacts.append(contact_data)
    
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(all_contacts, f, indent=4, ensure_ascii=False)

def load_all():
    """Lê todos os contactos guardados no ficheiro JSON"""
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def search(query: str):
    """Procura contactos no índice JSON pelo nome"""
    all_contacts = load_all()
    return [c for c in all_contacts if query.lower() in c['name'].lower()]