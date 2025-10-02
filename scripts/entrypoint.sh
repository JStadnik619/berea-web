#!/bin/bash

# BUG: Site can't be reached inside docker container
# TODO: Set logfile with --access-logfile=
gunicorn -w 4 --bind 0.0.0.0:80 'app:app'