FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY app/requirements.txt ./

RUN uv pip install -r requirements.txt --system


COPY app/ /app/

RUN ls -l /app

EXPOSE 8000

CMD ["uv", "run", "app.py", "--host=0.0.0.0"]
