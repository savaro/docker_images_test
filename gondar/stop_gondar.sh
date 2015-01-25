num=$1

if [ -z "$num" ]; then
    num=0
fi

container="gondar_$num"
if [[ `sudo docker ps` =~ "$container" ]]; then
    sudo docker exec $container service docker stop
    sudo docker stop $container
    echo container $container was stopped
else
    echo container $container is not running?
fi


