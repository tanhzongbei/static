static
====

Awesome project.


## Test

Install `nose` first:

    pip install nose

Run tests

    nosetests ./tests


## Debug

    mkdir -p /data/logs/static/
    python wsgiapp.py


## Run in production

    mkdir -p /data/logs/static/
    ./runuwsgi.sh start