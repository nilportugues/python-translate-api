FROM registry.gitlab.com/registry.docker.nilportugues.com/python3-ubuntu:1.0.0
RUN apt-get update && apt-get upgrade -y

# Install nginx
RUN apt-get install -y nginx


COPY ./translate_api-0.1.tar.gz /tmp/build.tar.gz
RUN pip3 install /tmp/build.tar.gz --upgrade

## Copy files for uwsgi
RUN mkdir -p /opt/uwsgi/
COPY ./uwsgi/uwsgi.ini /opt/uwsgi/uwsgi.ini
COPY ./uwsgi/app.wsgi /var/www/app.wsgi

## Copy files for nginx
COPY ./nginx/conf/app.conf /etc/nginx/sites-enabled/app.conf
RUN rm /etc/nginx/sites-enabled/default

# Exposed ports
EXPOSE 80

## Copy over the entrypoint
COPY ./entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
