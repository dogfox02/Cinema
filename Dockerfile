FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
   && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

WORKDIR /CinemaVersion1
RUN mkdir static
RUN mkdir media

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .