#!/bin/bash

src='/workspace/mathildetech/jakiro_ci'

echo 'copying code source'
sudo cp settings_internal.py $src/mathilde/
sudo cp manage_internal.py $src
sudo cp -r $src .

echo 'building jakiro image'
sudo mv Dockerfile_jakiro Dockerfile
sudo docker build -t index.alauda.io/chennanfei/jakiro_dev:latest .
sudo mv Dockerfile Dockerfile_jakiro

echo 'building jakiro internal APIs image'
sudo mv Dockerfile_jakiro_internal Dockerfile
sudo docker build -t index.alauda.io/chennanfei/jakiro_dev_internal:latest .
sudo mv Dockerfile Dockerfile_jakiro_internal

sudo rm -r jakiro_ci
