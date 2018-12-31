#!/bin/bash

DOCKER_CONTAINER=$([ ! -z "$1" ] && echo "$1" || echo "ucb-datalab-site")

echo "building site in container $DOCKER_CONTAINER"

docker build -t $DOCKER_CONTAINER .
