# distro os.
FROM ubuntu:focal
# mkdir users
LABEL maintainer="Takayuki Kamiyama <karuma.reason@gmail.com>"
# python 3.13.x
FROM python:3.13
# http://manpages.ubuntu.com/manpages/xenial/man7/debconf.7.html
ENV DEBCONF_NOWARNINGS=yes
# build package
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3-dev default-libmysqlclient-dev build-essential mariadb-client ca-certificates curl patch git
# install
RUN mkdir /mp4player
ENV APP_ROOT /mp4player
WORKDIR $APP_ROOT
ADD ./requirements.txt $APP_ROOT/requirements.txt
RUN pip3 install -r requirements.txt
ADD . $APP_ROOT
COPY . .
RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh
ADD . $APP_ROOT

COPY ./web/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

# EXPOSE 3000

# Start the main process.
CMD ["sh", "./web/start-server.sh"]
