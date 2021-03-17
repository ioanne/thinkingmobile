FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get install -y gcc \
  && apt-get install -y python-setuptools \
  && apt-get install -y python3-dev \
  && apt-get install -y libgdal-dev \
  && apt-get install -y libproj-dev \
  && apt-get install -y python3-mysqldb \
  && apt-get install -y default-libmysqlclient-dev \
  && apt-get install -y binutils

RUN pip install --upgrade pip

COPY ./requirements /requirements
RUN pip install -r requirements/local.txt

RUN mkdir /app
WORKDIR /app

COPY . /app
