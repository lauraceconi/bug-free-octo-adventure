SHELL := /bin/bash

docker_build:
	sudo docker build . --tag=encurtador:latest

docker_run:
	sudo docker run -i -t --rm -p 8000:8000 encurtador /bin/bash

migrate:
	python3 manage.py migrate

run:
	python3 manage.py runserver 0.0.0.0:8000

