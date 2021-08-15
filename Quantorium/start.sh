#!/bin/bash
source /var/www/qvantorium/Quantorium/env/bin/activate
exec gunicorn -c "/var/www/qvantorium/gunicorn_config.py" Quantorium.wsgi
