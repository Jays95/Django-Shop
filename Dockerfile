FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# Expose port
# Run manage.py runserver 127.0.0.1:8000

CMD python3 manage.py runserver 0.0.0.0:8000