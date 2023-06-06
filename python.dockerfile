FROM python:3.8-slim-buster

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Install pip requirements
COPY requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /ollivander
COPY . /ollivander

RUN useradd appuser && chown -R appuser /ollivander
USER appuser

RUN chmod a+x start.sh


CMD ["./start.sh"]