#!/bin/bash
#export variable for building the image
HOST_USER_GROUP_ARG=$(id -g $USER)
image_name="gaussian"
image_tag="latest"
docker build .\
    --tag "$image_name":"$image_tag" \
    --build-arg HOST_USER_GROUP_ARG=$HOST_USER_GROUP_ARG 
