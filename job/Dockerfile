FROM ubuntu:14.04

COPY requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /app
COPY . /app

CMD ["./run.sh"]
