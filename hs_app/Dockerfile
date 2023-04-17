# Dockerfile
FROM python:3.10
WORKDIR /hs_app
RUN pip install --upgrade pip
RUN pip install flask
COPY . /hs_app
ENV FLASK_APP=hs_app
CMD ["python","app.py"]