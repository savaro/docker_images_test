#!/bin/bash

container='jakiro_for_rubick_dev'
port=5000

if [[ `docker ps` =~ $container ]]; then
    echo container $container is running
elif [[ `docker ps -a` =~ $container ]]; then
    sudo docker start $container
else
    sudo docker run -d -p $port:5001 \
        --name $container \
	index.alauda.io/chennanfei/jakiro_dev:trusty
fi

sudo docker logs -f $container
