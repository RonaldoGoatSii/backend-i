from typer import Typer
from api.main import api
import uvicorn

app = Typer(
    name="FastAPI CLI"
)

@app.command()
def run():
    uvicorn.run(api)


@app.command()
def reques():
    ...

if __name__ == "__main__":
    app()