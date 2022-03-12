#!/bin/bash
APP=$(basename ${PWD})
docker rm -f ${APP}
docker run -it \
    --name=${APP} \
    -p 8080:80 \
    ${APP}