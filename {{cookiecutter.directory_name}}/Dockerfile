# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# copy requirements.txt
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# copy project
COPY . /app

ENTRYPOINT ["{{cookiecutter.file_name}}.py"]
