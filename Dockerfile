FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install net-tools ssh && \
    ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa && \
    apt-get -y install python python-pip && \
    pip install numpy pandas matplotlib plotly==4.1.0

COPY start.sh /start.sh
COPY iphost.py /iphost.py
COPY disk-usage.py /disk-usage.py
RUN chmod +x /start.sh

ENTRYPOINT ["./start.sh"]
