#! /bin/bash

cat access.log >> /usr/local/nginx/logs/access.log
cat pro.log >> /var/log/pro/pro.log
cat uwsgi.log >> /var/log/uwsgi.log
