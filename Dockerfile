FROM python:3.12-slim-bookworm

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    awscli \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

CMD ["python3", "app.py"]
