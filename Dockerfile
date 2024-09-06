FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk add postgresql-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT ["sh", "./scripts/setup.sh"]