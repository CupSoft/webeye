FROM python:3.10-alpine

WORKDIR /app

RUN pip install -U pip wheel setuptools
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]