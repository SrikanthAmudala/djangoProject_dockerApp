FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirement.txt
EXPOSE 8989
CMD exec gunicorn djangoProjectV1.wsgi:application — bind 0.0.0.0:8989 — workers 3