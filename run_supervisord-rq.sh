#!/usr/bin/env bash

source ~/.virtualenvs/opendims/bin/activate
cd $(dirname $0)
supervisord -n -c supervisord-rq.conf
