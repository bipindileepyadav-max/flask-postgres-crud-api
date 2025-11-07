FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y nano && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "/app/main.py"]
