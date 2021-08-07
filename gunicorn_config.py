command = '/var/www/qvantorium/env/bin/gunicorn'
pythonpath = '/usr/bin/python3'
bind = '127.0.0.1:8001'
workers = 3
user = 'kirill'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=Quantorium.settings'
