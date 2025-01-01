FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
    netcat \
    supervisor \
    nginx \
    gnupg \
    curl \
    && rm -rf /var/lib/apt/lists/*


RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf


COPY requirements/common.txt /tmp/common.txt

RUN pip install -Ur /tmp/common.txt

ENV APP_HOME=/app

WORKDIR $APP_HOME
COPY ./scripts_docker/start-container.sh /usr/local/bin/start-container.sh
RUN chmod +x /usr/local/bin/start-container.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


COPY ./app $APP_HOME/app
COPY ./alembic $APP_HOME/alembic
COPY ./alembic.ini $APP_HOME/alembic.ini
EXPOSE 8000

ENTRYPOINT ["start-container.sh"]
