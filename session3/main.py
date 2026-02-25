from typer import Typer, echo, style, colors
from datetime import datetime

cli = Typer()

@cli.command()
def greetings(name: str, surname = ""):
    echo(style(f"Greetings {name and surname}", fg=colors.BLUE))

@cli.command()
def goodbye():
    echo(style("Goodbye!", fg=colors.YELLOW))

if __name__ == "__main__":
    cli()
