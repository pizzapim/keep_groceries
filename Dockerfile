FROM python:3

RUN apt-get update && apt-get -y install cron

WORKDIR /usr/src/app

COPY script.py ./
COPY environ ./
COPY script-cron /etc/cron.d/script-cron

RUN chmod 0644 /etc/cron.d/script-cron
RUN crontab /etc/cron.d/script-cron
RUN touch /var/log/cron.log
RUN pip install gkeepapi

CMD cron && tail -f /var/log/cron.log
