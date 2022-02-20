FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /Slueth_hound.io/requirements.txt

WORKDIR /Slueth_hound.io/

COPY Pipfile Pipfile.lock /Slueth_hound.io/
RUN pip install pipenv
RUN pipenv install --system
RUN pip install -r requirements.txt

COPY . /Slueth_hound.io/