#! /bin/bash

python manage.py makemigration
python manage.py migrate
python manage.py createsuper user
python manage.py runserver
