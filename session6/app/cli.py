import typer
from app.services.meeting_service import create_meeting, list_meetings
from app.core.logging_config import configure_logging

configure_logging()

app = typer.Typer()


@app.command("create-meeting")
def create_meeting_cmd(title: str, date: str, owner: str) -> None:
    meeting = create_meeting(title, date, owner)
    typer.echo(f"Created: {meeting.id}")


@app.command("create-meeting")
def create_meeting_cmd(
    title: str = typer.Option(..., help="Meeting title"),
    date: str = typer.Option(..., help="Meeting date (YYYY-MM-DD)"),
    owner: str = typer.Option(..., help="Meeting owner"),
) -> None:
    meeting = create_meeting(title, date, owner)
    typer.echo(f"Created: {meeting.id}")


if __name__ == "__main__":
    app()