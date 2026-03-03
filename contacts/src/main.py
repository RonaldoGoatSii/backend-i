import typer
from services import numbers
cli = typer.Typer()

@cli.command()
def create(
    name:str,
    number:str,
)->None:
    contact.create(name, number)

if __name__ == "__main__":
    cli()
