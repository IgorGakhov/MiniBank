FROM python:3.11-slim

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY alembic.ini /app/alembic.ini
COPY src /app/src

CMD alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
