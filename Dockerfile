FROM python:3
WORKDIR /encurtador
RUN apt-get update && apt-get install -y \
    python3-pip \
    make

RUN pip install --no-cache-dir Django==2.2.1

COPY . /encurtador
CMD ["python", "./manage.py", "migrate"]
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
