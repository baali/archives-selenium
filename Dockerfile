FROM python:3.7

WORKDIR /opt

ADD webtests.py /opt
ADD entrypoint.sh /opt
ADD requirements.txt /opt

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash", "-c", "/opt/entrypoint.sh"]
