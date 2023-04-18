# syntax=docker/dockerfile:1
FROM python:3.11-slim-bullseye

RUN mkdir /data
ARG UNAME=hsagar2
ARG UID=9529
ARG GID=9529
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
RUN chown -R $UNAME:$UNAME /data

USER $UNAME
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install Flask
RUN pip install -r requirements.txt
RUN chown -R $UNAME:$UNAME /data
EXPOSE 5000
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

