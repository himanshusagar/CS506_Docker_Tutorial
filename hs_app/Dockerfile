# Dockerfile
FROM python:3.9
WORKDIR /hs_app
COPY . /hs_app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=hs_app
CMD ["python","app.py"]