FROM python:3.7-slim-buster

WORKDIR /api

RUN apt-get update && apt-get install -y python3

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "fast_api:api"]