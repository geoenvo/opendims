#!/usr/bin/env bash

source ~/.virtualenvs/opendims/bin/activate
cd $(dirname $0)/opendims
python manage.py runserver 0.0.0.0:8000
