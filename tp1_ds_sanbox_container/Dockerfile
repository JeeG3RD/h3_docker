FROM ubuntu

WORKDIR /workspace

COPY requirements.txt /

RUN apt-get update && \
apt-get install python3 python3-pip  vim git -y && \
pip3 install --upgrade pip && \
pip3 install -r /requirements.txt && \
git config --global user.name JonDoe && \ 
git config --global user.email jon@doe.com && \ 
git clone https://github.com/JeeG3RD/h3_docker.git

EXPOSE 8000

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]