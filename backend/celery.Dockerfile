FROM python:3.10-alpine as smallimage
RUN pip install -U pip wheel setuptools
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .
CMD ["celery", "-A", "app.core.celery_app", "worker", "-l", "info"]