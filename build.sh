APP=$(basename ${PWD})
docker rmi ${APP}
docker build -t ${APP} .