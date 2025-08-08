# Pull official base image
FROM python:3.10-slim

# Install the requirements packages
RUN apt-get update && apt-get install apt-utils libpq-dev gcc -y

# Install dependencies
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Copy project
COPY . /usr/src/app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
ENV FLASK_APP server.py
ENV FLASK_DEBUG 1

# Variables ocultas del fichero .env
ENV HOSTNAME=${HOSTNAME}

ENV POSGRESQL_DATABASE=${POSGRESQL_DATABASE}
ENV POSGRESQL_URL=${POSGRESQL_URL}
ENV POSGRESQL_PORT=${POSGRESQL_PORT}
ENV POSGRESQL_USER=${POSGRESQL_USER}
ENV POSGRESQL_USER_PASSWORD=${POSGRESQL_USER_PASSWORD}


# Export port
EXPOSE ${DOCKER_BACKEND_PORT}

# Start
ENTRYPOINT ["sh","/usr/src/app/gunicorn.sh"]

