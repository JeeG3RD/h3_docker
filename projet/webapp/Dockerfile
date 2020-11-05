FROM python:3.7-slim-buster

WORKDIR /application
COPY . .

RUN apt-get update && \
apt-get install python3 python3-pip -y && \
pip3 install --upgrade pip && \
pip3 install -r requirements.txt

CMD streamlit run app.py --server.port $PORT