import typer
from app.domain.models import Meeting, ActionItem
from app.services.memory_store import meetings

app = typer.Typer()

@app.command()
def seed():
    """Adiciona dados de teste para verificar o modelo."""
    item = ActionItem(description="Enviar relatório", owner="Tiago", due_date="2026-03-01")
    reuniao = Meeting(id="1", title="Sincronização", date="2026-02-25", owner="Tiago", action_items=[item])
    meetings.append(reuniao)
    print("Dados de teste criados com sucesso!")

@app.command()
def list_meetings():
    """Exercício: Listar reuniões com output legível."""
    if not meetings:
        print("Nenhuma reunião encontrada. Corre o comando 'seed' primeiro.")
        return
    
    for m in meetings:
        print(f"\nID: {m.id} | Título: {m.title} ({m.date})")
        print(f"Dono: {m.owner}")
        print(f"Tarefas ({len(m.action_items)}):")
        for item in m.action_items:
            print(f"  - [{item.status}] {item.description} (Resp: {item.owner})")

if __name__ == "__main__":
    app()