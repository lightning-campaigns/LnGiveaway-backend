FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

RUN #export DOCKER_DEFAULT_PLATFORM=linux/amd64
ENV DOCKER_DEFAULT_PLATFORM=linux/amd64


LABEL maintainer="omoniyi24@gmail.com"

#CMD ["python", "app.py", "run", "-h", "0.0.0.0"]
