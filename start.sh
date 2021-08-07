#!/bin/bash
cd /var/www/Quantorium/
exec gunicorn -c "gunicorn_config.py" Quantorium.wsgi
