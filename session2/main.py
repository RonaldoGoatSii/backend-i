import typer
from app.domain.models import Meeting, ActionItem
from app.services.memory_store import meetings

app = typer.Typer()

@app.command()
def seed():
    item = ActionItem(description="Enviar relatório", owner="Tiago", due_date="2026-03-01")
    reuniao = Meeting(id="1", title="Sincronização", date="2026-02-25", owner="Tiago", action_items=[item])
    meetings.append(reuniao)
    print("Dados de teste criados com sucesso!")

@app.command()
def list_meetings():
    if not meetings:
        print("Nenhuma reunião encontrada. Corre o comando 'seed' primeiro.")
        return
    
    for m in meetings:
        print(f"\nID: {m.id} | Title: {m.title} ({m.date})")
        print(f"Owner: {m.owner}")
        print(f"Items ({len(m.action_items)}):")
        for item in m.action_items:
            print(f"Summary  - [{item.status}] {item.description} (Resp: {item.owner})")

if __name__ == "__main__":
    app()