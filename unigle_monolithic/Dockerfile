# pull official base image
FROM python:3.9.6-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# copy project
COPY . .

# run project
# RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
# CMD python manage.py runserver 0.0.0.0:8000

# expose port
# EXPOSE 8000
