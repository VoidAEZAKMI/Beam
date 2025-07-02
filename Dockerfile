FROM python:3.12.1-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2

WORKDIR /app

RUN apk add --no-cache python3-dev gcc musl-dev libpq-dev


COPY pyproject.toml poetry.lock* /app/

RUN pip install --upgrade pip && \
    pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.create false && \
    poetry lock --no-interaction --no-ansi && \
    poetry install --no-root --without dev --no-interaction --no-ansi

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY . /app/

ENTRYPOINT ["/entrypoint.sh"]