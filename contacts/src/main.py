import typer
from services import numbers
cli = typer.Typer()

@cli.command()
def create(
    name:str,
    number:str,
)->None:
    numbers.create(name, number)

if __name__ == "__main__":
    cli()
