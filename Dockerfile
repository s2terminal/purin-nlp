FROM python:3.10-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install
