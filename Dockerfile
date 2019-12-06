FROM python:3-alpine

ADD . /app


WORKDIR /app

RUN pip install redis 


CMD ["python","app.py"]


