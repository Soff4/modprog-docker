FROM python:3.12
ADD main.py .
RUN pip install psutil
CMD ["python", "./main.py"]