SHELL := /bin/bash

setup:
	sudo docker build . --tag=encurtador:latest

run:
	docker run --rm -p 8000:8000 encurtador
