# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "sql_app.main:app" , "--host", "0.0.0.0", "--port", "90", "--proxy-headers"]