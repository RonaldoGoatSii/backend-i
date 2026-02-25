from typer import Typer, echo,style,colors
from datetime import datetime

cli = Typer()

@cli.command()
def greetings():
    echo(style("Greetig", fg=colors.BLUE))

@cli.command()
def goodbye():
    echo(style("Goodbye!", fg=colors.YELLOW))



if __name__ == "__main__":
    cli()
