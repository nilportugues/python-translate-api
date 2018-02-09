FROM registry.gitlab.com/registry.docker.nilportugues.com/python3-ubuntu:1.0.0

# Install nginx
RUN echo 'deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx' >>  /etc/apt/sources.list.d/nginx.list
RUN echo 'deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx' >>  /etc/apt/sources.list.d/nginx.list

RUN apt-get update -y && apt-get upgrade -y 
RUN apt-get install -y --allow-unauthenticated nginx nano curl 

COPY ./docker/translate_api-0.1.tar.gz /tmp/build.tar.gz
RUN pip3 install /tmp/build.tar.gz --upgrade

## Copy files for uwsgi
RUN mkdir -p /opt/uwsgi/
COPY ./docker/uwsgi/uwsgi.ini /opt/uwsgi/uwsgi.ini
COPY ./docker/uwsgi/app.wsgi /var/www/app.wsgi

## Copy files for nginx
 COPY ./docker/nginx/conf/app.conf /etc/nginx/sites-enabled/app.conf
# RUN rm /etc/nginx/sites-enabled/default

# Exposed ports
EXPOSE 80

## Copy over the entrypoint
COPY ./docker/entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
