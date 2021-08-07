#!/bin/bash
cd /var/www/qvantorium/
source /var/www/qvantorium/Quantorium/env/bin/activate
exec gunicorn -c "gunicorn_config.py" Quantorium.wsgi
