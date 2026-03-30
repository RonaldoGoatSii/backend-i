import typer
import uuid
from app.core import storage
from app.services import report_service

app = typer.Typer(help="Meeting Manager CLI")

@app.command()
def create_meeting(title: str, date: str, owner: str):
    meetings = storage.load_meetings()
    new_meeting = {
        "id": str(uuid.uuid4())[:8],
        "title": title,
        "date": date,
        "owner": owner,
        "action_items": [] # Começa vazio
    }
    meetings.append(new_meeting)
    storage.save_meetings(meetings)
    typer.echo(f"Reunião '{title}' criada! ID: {new_meeting['id']}")

@app.command()
def list_meetings():
    meetings = storage.load_meetings()
    if not meetings:
        typer.echo("Nenhuma reunião encontrada.")
        return
    for m in meetings:
        typer.echo(f"[{m['id']}] {m['date']} - {m['title']} ({m['owner']})")

@app.command()
def report(from_date: str = None, to_date: str = None):
    meetings = storage.load_meetings()
    if from_date and to_date:
        res = report_service.get_period_report(meetings, from_date, to_date)
        typer.echo(f"Relatório de {from_date} a {to_date}:")
    else:
        res = report_service.get_summary(meetings)
        typer.echo("Resumo Geral:")
    
    typer.echo(f" - Total: {res['total']} reuniões\n - Tarefas: {res['tasks']}")