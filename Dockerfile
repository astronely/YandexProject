FROM python:3.10.6-alpine
WORKDIR /mysite
COPY ./ /mysite
RUN apk update && pip install -r /mysite/requirements.txt
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]