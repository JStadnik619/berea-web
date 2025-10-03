#!/bin/bash

# TODO: Log to a file instead of std-out
gunicorn -w 4 --bind 0.0.0.0:8000 'app:app' --access-logfile=-