#!/bin/sh
flask db upgrade
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
gunicorn --bind 0.0.0.0:5000 wsgi 