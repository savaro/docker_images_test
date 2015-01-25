#!/bin/bash

#sudo wrapdocker &
sudo service docker start

sudo sleep 5

sudo docker login --username='' --password='' --email='' index.alauda.io

sudo python build_demo/worker.py
