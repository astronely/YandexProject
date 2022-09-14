FROM python:3.10.6-alpine
WORKDIR /mysite
COPY ./ /mysite
RUN apk update && pip install -r /mysite/requirements.txt --no-cache-dir
EXPOSE 8000
CWD ["python", "manage.py", "runserver", "0.0.0.0:8000"]