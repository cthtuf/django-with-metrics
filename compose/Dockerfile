FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /code
EXPOSE 8000

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        jq \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade \
        pip \
        setuptools \
        wheel

COPY compose/requirements.txt /deps/requirements.txt
RUN pip install -r /deps/requirements.txt

COPY . /code

ENTRYPOINT /code/manage.py runserver 0.0.0.0:8000
