FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY ./app /app

RUN pip install --upgrade pip

RUN \
 apt-get update --fix-missing && \
 apt-get -y install libpq-dev gcc && \
 pip install --upgrade pip && \
 pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["bash", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 80 --reload"]