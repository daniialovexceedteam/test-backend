FROM python:3.8
ENV DOCKER_BUILDKIT=0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY . /code/

RUN pip install poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt