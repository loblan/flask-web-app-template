APP=$(basename ${PWD})
rm -rf app/__pycache__
rm -rf .env
docker rm -f ${APP}
docker rmi ${APP}
