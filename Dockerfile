FROM python:3.7-alpine

COPY requirements/* /tmp/

RUN pip install -r /tmp/dev.txt

RUN rm /tmp/*.txt

RUN adduser -D -s /bin/sh appuser

USER appuser

WORKDIR /opt
