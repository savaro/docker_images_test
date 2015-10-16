FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    python-pip \
    python-dev \
    libpq-dev \
    curl

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run.sh .
RUN chmod +x run.sh
CMD ["/run.sh"]

WORKDIR /app
COPY . /app
