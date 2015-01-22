#!/bin/bash

sudo cp -r /workspace/mathildetech/gondar .
sudo docker build -t index.alauda.io/chennanfei/gondar .

sudo rm -r gondar
