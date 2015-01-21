#!/bin/bash

redis-server &

python manage_internal.py runserver 0.0.0.0:5001
