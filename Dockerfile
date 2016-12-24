FROM python:3-onbuild

MAINTAINER knarfeh@outlook.com

WORKDIR /print_logs

COPY . /print_logs

RUN chmod +x /print_logs/print_log.sh

CMD ["/print_logs/print_log.sh"]
