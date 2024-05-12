FROM python:3.12

WORKDIR /app

ADD main.py .

RUN pip install psutil

CMD ["python", "./main.py"]