FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install net-tools ssh
RUN ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
RUN apt-get -y install python python-pip
RUN pip install numpy pandas matplotlib

COPY start.sh /start.sh
COPY ipaddress.py /ipaddress.py
RUN chmod +x /start.sh

ENTRYPOINT ["./start.sh"]
