FROM python:3.11.4

WORKDIR /app

COPY . /app/

RUN pip --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]

