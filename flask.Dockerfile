FROM python:3.9

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirement-flask.txt /app/requirement-flask.txt
RUN pip install -r requirement-flask.txt
