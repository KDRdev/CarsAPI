FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /cars_api
WORKDIR /cars_api
ADD . /cars_api/
RUN pip install -r requirements.txt
