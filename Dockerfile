FROM python:3-alpine

ENV PYPYTHONUNBUFFERED "1"
ENV PYTHONDONTWRITEBYTECODE "1"

RUN apt update -yyq && apt install git -yyq


