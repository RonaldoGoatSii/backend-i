FROM python:3.14

RUN pip install uv

WORKDIR /api

COPY . .

RUN uv sync

CMD uv run python src/cli.py run