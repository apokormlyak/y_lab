FROM python:3.10-alpine

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev

WORKDIR /app

COPY requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .