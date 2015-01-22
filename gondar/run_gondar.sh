#!/bin/bash

num=$1

if [ -z $num ]; then
    num='0'
fi

container="gondar.$num"
image_repo='gondar'
image_tag='latest'

if [[ `sudo docker ps` =~ /^$container$/ ]]; then
    echo container $container is running
elif [[ `sudo docker ps -a` =~ /^$container/ ]]; then
    echo container $container was stopped. Starting...
    sudo docker start $container
else
    sudo docker run -d --privileged \
        --name $container \
	index.alauda.io/chennanfei/$image_repo:$image_tag
fi

sudo docker logs -f $container
