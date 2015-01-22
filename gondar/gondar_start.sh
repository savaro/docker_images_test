#!/bin/bash

sudo wrapdocker &
sudo sleep 3

sudo docker -d &

# wait 10 seconds till docker is started
sudo sleep 10

sudo docker login --username='' --password='' --email='' index.alauda.io

sudo python build_demo/worker.py
