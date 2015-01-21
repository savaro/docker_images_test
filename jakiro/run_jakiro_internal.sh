#!/bin/bash

container='jakiro_dev_internal'
image_repo='jakiro_dev_internal'
image_tag='latest'
port=81

if [[ `docker ps` =~ $container ]]; then
    echo container $container is running
elif [[ `docker ps -a` =~ $container ]]; then
    sudo docker start $container
else
    sudo docker run -d --volumes-from jakiro_dev -p $port:5001 \
        --name $container \
	index.alauda.io/chennanfei/$image_repo:$image_tag
fi

sudo docker logs -f $container
