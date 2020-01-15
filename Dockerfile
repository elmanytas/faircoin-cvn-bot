FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean
RUN apt-get -y install python3-pip && \
    apt-get clean
RUN mkdir /opt/faircoin-cvn-bot/
ADD . /opt/faircoin-cvn-bot/
RUN pip3 install errbot
RUN pip3 install python-telegram-bot
RUN pip3 install python-bitcoinrpc

CMD ["env", "LC_ALL=C.UTF-8", "errbot", "-c", "/opt/faircoin-cvn-bot/config.py"]
