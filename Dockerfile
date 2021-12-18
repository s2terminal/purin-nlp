FROM python:3.10-slim

WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# TransformersのインストールにRustコンパイラが要求される
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

RUN pip install poetry

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install
