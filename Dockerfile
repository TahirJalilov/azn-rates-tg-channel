FROM python:latest

RUN apt-get update && apt-get -y install cron vim && apt-get autoremove -y
WORKDIR /src
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src
CMD bash -c "cron"
