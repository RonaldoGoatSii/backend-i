import typer


import datetime

app = typer.Typer()

@app.command()
def create_meeting(title: str, date: str, owner: str) -> None:
    typer.echo("✅ Meeting Created!")
    typer.echo(f"Title: {title}")
    typer.echo(f"Date: {date}")
    typer.echo(f"Owner: {owner}")

if __name__ == "__main__":
    app()