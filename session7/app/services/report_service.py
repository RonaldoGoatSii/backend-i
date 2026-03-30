from datetime import datetime

def get_summary(meetings: list) -> dict:
    return {
        "total": len(meetings),
        "tasks": sum(len(m.get("action_items", [])) for m in meetings)
    }

def get_period_report(meetings: list, from_date: str, to_date: str) -> dict:
    start = datetime.strptime(from_date, "%Y-%m-%d")
    end = datetime.strptime(to_date, "%Y-%m-%d")
    
    filtered = [
        m for m in meetings 
        if start <= datetime.strptime(m["date"], "%Y-%m-%d") <= end
    ]
    return get_summary(filtered)