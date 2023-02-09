FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

RUN flask db upgrade
RUN flask create-admin
RUN flask create-tags

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]