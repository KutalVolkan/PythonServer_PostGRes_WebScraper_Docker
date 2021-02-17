# build this image
FROM python:latest
# see output of application in real-time
ENV PYTHONUNBUFFERED = 1
# working directory, creates one if not exist
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
