XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

docker run --rm -it \
        --net=host \
        --privileged \
        -v /dev/bus/usb:/dev/bus/usb \
        --device /dev/bus/usb:/dev/bus/usb \
        --volume=$XSOCK:$XSOCK:rw \
        --volume=$XAUTH:$XAUTH:rw \
        --volume=/Users/matteocassinelli/ROS\ sonar\ package:/catkin_ws/src/sonar \
        --env="XAUTHORITY=${XAUTH}" \
        --env="DISPLAY" \
    	sonar