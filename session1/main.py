import typer

app = typer.Typer()

@app.command("hi")
def create_meeting(title: str, date: str, owner: str) -> None:
    typer.echo(f"Hello from Typer!!!")

if __name__ == "__main__":
    app()