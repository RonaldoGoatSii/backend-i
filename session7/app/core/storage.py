import json
import os

DATABASE_FILE = "meetings_db.json"

def load_meetings() -> list:
    if not os.path.exists(DATABASE_FILE):
        return []
    with open(DATABASE_FILE, "r") as f:
        return json.load(f)

def save_meetings(meetings: list):
    with open(DATABASE_FILE, "w") as f:
        json.dump(meetings, f, indent=4)