SHELL := /bin/bash

setup:
	python3 -m venv env
	source env/bin/activate
	env/bin/pip3 install Django==2.2.1
	#python3 manage.py migrate
	#source env/bin/deactivate

run:
	source env/bin/activate
	python3 manage.py runserver 0.0.0.0:8000
	xdg-open http://localhost:8000

