FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Slueth_hound.io/

COPY Pipfile Pipfile.lock /Slueth_hound.io/
RUN pip install pipenv && pipenv install --system

COPY . /Slueth_hound.io/