FROM ubuntu
WORKDIR /application
COPY . /application

RUN apt-get update && \
apt-get install python3 python3-pip -y && \
pip3 install --upgrade pip && \
pip3 install -r requirements.txt

CMD streamlit run main.py