#!/bin/bash
rm -rf anorakapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations anorakapi
python3 manage.py migrate anorakapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata whiskeys
python3 manage.py loaddata tags
python3 manage.py loaddata whiskey_tags
python3 manage.py loaddata userwhiskeys