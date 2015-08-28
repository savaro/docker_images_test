FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-pip python-dev

COPY requirements.txt .
RUN pip install -r /requirements.txt

EXPOSE 8081
CMD ["/bin/bash"]
