# Dockerfile
FROM python:3.10-slim

RUN mkdir /organization

COPY requirements.txt /organization/requirements.txt
COPY src/ /organization/src
COPY src/main.py /organization/main.py
COPY __init__.py /organization/__init__.py

WORKDIR /organization

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
