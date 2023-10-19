FROM python:3.12-alpine3.18

WORKDIR /src
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . ./

CMD [ "python", "./azn_rates_tg_channel/main.py" ]