FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    python-pip \
    python-dev \
    libpq-dev \
    curl

COPY requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /app
COPY . /app

CMD ["./run.sh"]
