FROM python:3.9-buster

ENV PYTHONUNBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code

RUN mkdir /code/
WORKDIR /code
COPY .devcontainer/requirements.txt /code
#COPY . /code

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt