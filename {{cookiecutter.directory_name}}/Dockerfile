# syntax=docker/dockerfile:1

FROM python:3.11.9-slim

# Install Poetry
RUN pip install poetry

# Disable virtualenv creation
RUN poetry config virtualenvs.create false

# Set working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock file
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy project
COPY src/ .
COPY .env .

ENTRYPOINT ["python", "-u", "{{cookiecutter.file_name}}.py"]
