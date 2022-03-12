FROM python

WORKDIR /code
COPY ./app /code/app

COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./gunicorn_conf.py /code/
CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:80", "app"]