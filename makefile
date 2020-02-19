SHELL := /bin/bash

setup:
	sudo docker build . --tag=encurtador:latest

run:
	sudo docker run --rm -p 8000:8000 encurtador

container:
	sudo docker run -i -t --rm -p 8000:8000 encurtador /bin/bash

test:
	python manage.py test
