from dataclasses import asdict
import json
from pathlib import Path

from data.models import Meeting,MeetingMetadata
from uuid import uuid4


BASE_PATH = Path ("meetings")
INDEX_PATH = Path("meetings/index.json")

def create(meeting:Meeting):
    filename = f"{BASE_PATH}/{uuid4()}.md"
    with open(filename,"w") as file:
        file.writelines(str(meeting))

    
    if not INDEX_PATH.exists():
        INDEX_PATH.touch()
        INDEX_PATH.write_text("[]")

    index_content = None

    with open(INDEX_PATH.absolute(),"r") as file:
        index_content:list = json.loads(file.read())

    index_content.append(
        asdict(MeetingMetadata(
            meeting=meeting,
            path=filename
        ))
    )
    
    with open(INDEX_PATH,"w") as file:
        json.dump(index_content,file)






# import json
# import os
# from dataclasses import asdict




# JSON_FILE = "src/data/index.json"

# def create(meeting: Meeting):
#     # 1. Garante que as pastas existem
#     os.makedirs(BASE_PATH, exist_ok=True)
#     os.makedirs("src/data", exist_ok=True)
    
#     # 2. Criar o ficheiro Markdown (ID único)
#     md_id = str(uuid4())
#     filename = f"{BASE_PATH}/{md_id}.md"
    
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(str(meeting))

#     # 3. Atualizar o Índice JSON
#     data = load_all()
    
#     meeting_dict = asdict(meeting)
#     meeting_dict["id"] = md_id  
    
#     data.append(meeting_dict)
    
#     with open(JSON_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)

# def load_all():
#     """Lê todas as reuniões do JSON"""
#     if not os.path.exists(JSON_FILE):
#         return []
#     try:
#         with open(JSON_FILE, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (json.JSONDecodeError, IOError):
#         return []

# def search(query: str):
#     """Procura no JSON pelo título"""
#     all_data = load_all()
#     return [m for m in all_data if query.lower() in m['title'].lower()]
        

