FROM ubuntu:14.04
MAINTAINER knarfeh@outlook.com

# Update
RUN apt-get update && apt-get install -y \
        python-dev \
        libpq-dev \
        libsasl2-dev \
        libldap2-dev

RUN curl https://bootstrap.pypa.io/get-pip.py | python

COPY . /print_logs
WORKDIR /print_logs
RUN chmod +x /print_logs/print_log.sh

CMD ["/bin/bash"]
