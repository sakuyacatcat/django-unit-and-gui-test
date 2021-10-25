# Use debian base image
FROM python:3.8.12-slim-bullseye

# update, and install packages, and remove cache
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libxml2-dev libxslt1-dev libmariadb-dev default-libmysqlclient-dev && \
    pip3 install -U pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /usr/bin/mysqld* /usr/bin/mysql*

# setup python env
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8

# prepare app root directory
ENV ROOT_PATH /app
RUN mkdir ${ROOT_PATH}
WORKDIR ${ROOT_PATH}

# transfer local django dev env
COPY . ${ROOT_PATH}

# install common library for Django application
RUN pip3 install -r requirements/base.txt

# start application script
COPY scripts/entrypoint.sh /usr/bin
RUN chmod +x /usr/bin/entrypoint.sh
CMD [ "entrypoint.sh" ]
