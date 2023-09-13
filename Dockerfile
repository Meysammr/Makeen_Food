FROM python:3.10
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -U pip

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary


COPY . /code/

EXPOSE 8000


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

CMD gunicorn Makeen-Food.wsgi:application -bind 0.0.0.0:8000 workers 4