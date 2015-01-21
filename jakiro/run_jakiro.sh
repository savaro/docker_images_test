#!/bin/bash

container='jakiro_dev'
code_src='jakiro_ci'
image_repo='jakiro_dev'
image_tag='latest'
port=80

if [[ `sudo docker ps` =~ /^$container$/ ]]; then
    echo container $container is running
elif [[ `sudo docker ps -a` =~ /^$container/ ]]; then
    echo container $container was stopped. Starting...
    sudo docker start $container
else
    sudo docker run -d -p $port:5001 \
        -v /workspace/mathildetech/$code_src:/jakiro \
        --name $container \
	index.alauda.io/chennanfei/$image_repo:$image_tag
fi

sudo docker logs -f $container
