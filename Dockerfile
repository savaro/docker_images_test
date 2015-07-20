FROM ubuntu:14.04

COPY requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["bash"]
