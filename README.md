# Flask web app template

Basic flask web app template with helper scripts and docker project to host with gunicorn.

## Flask

### Setup virtual environnement

    rm -rf .env
    python -m venv .env
    .env/Scripts/activate
    pip install --no-cache-dir --upgrade -r requirements.txt

### Start flask in debug mode

    FLASK_APP=app FLASK_DEBUG=1 python -m flask run

## Docker

### Build

    APP=$(basename ${PWD})
    docker rmi ${APP}
    docker build -t ${APP} .

### Run

    APP=$(basename ${PWD})
    docker rm -f ${APP}
    docker run -it \
        --name=${APP} \
        -p 8080:80 \
        ${APP}