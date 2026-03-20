from app.core.errors import ValidationError
from app.core.validators import validate_iso_date


try:
    validate_iso_date(due_date)
    # chamar o serviço que cria a tarefa

except ValidationError as exc:
    typer.echo(f"Validation error: {exc}")
    raise typer.Exit(code=2)