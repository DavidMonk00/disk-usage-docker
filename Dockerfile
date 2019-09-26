FROM alpine:latest

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk upgrade
RUN apk add net-tools openssh gcc g++
RUN ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
RUN apk add python3 python3-dev py3-pip
RUN pip3 install --upgrade pip setuptools
RUN pip3 install numpy

COPY start.sh /start.sh
COPY ipaddress.py /ipaddress.py
RUN chmod +x /start.sh

ENTRYPOINT ["./start.sh"]
